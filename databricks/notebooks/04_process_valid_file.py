# 04 - Process a validated file

from pyspark.sql import functions as F

dbutils.widgets.text("input_path", "/mnt/staging/instruments/")
input_path = dbutils.widgets.get("input_path")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(input_path)
)

processed_df = (
    df
    .withColumn("source_file_name", F.element_at(F.split(F.input_file_name(), "/"), -1))
    .withColumn("ingestion_timestamp", F.current_timestamp())
    .withColumn("validation_status", F.lit("VALIDATED"))
)

display(processed_df.limit(20))
