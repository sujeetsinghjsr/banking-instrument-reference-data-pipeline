# 02 - Validate duplicate rows

dbutils.widgets.text("input_path", "/mnt/landing/instruments/")
input_path = dbutils.widgets.get("input_path")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(input_path)
)

total_count = df.count()
distinct_count = df.dropDuplicates().count()
duplicate_count = total_count - distinct_count

validation_status = "FAIL" if duplicate_count > 0 else "PASS"

print({
    "file_path": input_path,
    "total_count": total_count,
    "duplicate_count": duplicate_count,
    "validation_status": validation_status
})
