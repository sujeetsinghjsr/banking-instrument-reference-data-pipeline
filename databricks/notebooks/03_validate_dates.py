# 03 - Metadata-driven date validation

from pyspark.sql import functions as F

dbutils.widgets.text("input_path", "/mnt/landing/instruments/")
input_path = dbutils.widgets.get("input_path")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(input_path)
)

# In production, load these rules from Azure SQL using JDBC and a secure
# Key Vault / managed-identity based connection.
validation_rules = [
    {"column_name": "trade_date", "expected_format": "yyyy-MM-dd"},
    {"column_name": "maturity_date", "expected_format": "yyyy-MM-dd"},
    {"column_name": "settlement_date", "expected_format": "yyyy-MM-dd"}
]

invalid_conditions = []

for rule in validation_rules:
    column_name = rule["column_name"]
    expected_format = rule["expected_format"]

    if column_name in df.columns:
        invalid_conditions.append(
            F.to_date(F.col(column_name), expected_format).isNull()
            & F.col(column_name).isNotNull()
            & (F.trim(F.col(column_name)) != "")
        )

if invalid_conditions:
    combined_condition = invalid_conditions[0]
    for condition in invalid_conditions[1:]:
        combined_condition = combined_condition | condition

    invalid_date_count = df.filter(combined_condition).count()
else:
    invalid_date_count = 0

validation_status = "FAIL" if invalid_date_count > 0 else "PASS"

print({
    "invalid_date_count": invalid_date_count,
    "validation_status": validation_status
})
