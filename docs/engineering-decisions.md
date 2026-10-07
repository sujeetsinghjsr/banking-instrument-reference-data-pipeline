# Engineering Decisions

## Why ADLS Gen2?

Scalable cloud object storage with a separation between storage and compute.

## Why Azure Data Factory?

ADF provides orchestration, scheduling, parameterization and integration across Azure services.

## Why Databricks?

Databricks with Apache Spark is appropriate for scalable data processing and complex validation logic.

## Why Delta Lake?

Delta provides transactional table storage, schema enforcement and reliable processing patterns on the data lake.

## Why Azure SQL for validation metadata?

Validation rules are configuration rather than transformation logic. Keeping them in Azure SQL makes the rules changeable without modifying the core processing framework.

## Why separate landing, staging and rejected zones?

The separation improves traceability, troubleshooting, reprocessing and operational control.

## Why Key Vault?

Secrets should not be embedded in notebooks, configuration files or Git repositories.

## Production considerations

A production implementation should additionally consider idempotency, schema evolution, audit logging, lineage, monitoring, retry/recovery, access control, encryption, CI/CD, automated data-quality reporting, partitioning and performance tuning.
