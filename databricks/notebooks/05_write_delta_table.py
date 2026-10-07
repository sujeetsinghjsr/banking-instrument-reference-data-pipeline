# 05 - Write validated records to Delta

from pyspark.sql import functions as F

dbutils.widgets.text("input_path", "/mnt/staging/instruments/")
dbutils.widgets.text("target_table", "reference_data.instrument_reference")

input_path = dbutils.widgets.get("input_path")
target_table = dbutils.widgets.get("target_table")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(input_path)
)

final_df = (
    df
    .withColumn("source_file_name", F.element_at(F.split(F.input_file_name(), "/"), -1))
    .withColumn("ingestion_timestamp", F.current_timestamp())
    .withColumn("validation_status", F.lit("VALIDATED"))
)

(
    final_df.write
    .format("delta")
    .mode("append")
    .saveAsTable(target_table)
)

print(f"Written to Delta table: {target_table}")
