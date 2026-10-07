# 01 - Read landing file

from pyspark.sql import functions as F

dbutils.widgets.text("input_path", "/mnt/landing/instruments/")
input_path = dbutils.widgets.get("input_path")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(input_path)
)

print(f"Input columns: {df.columns}")
print(f"Input record count: {df.count()}")

display(df.limit(20))
