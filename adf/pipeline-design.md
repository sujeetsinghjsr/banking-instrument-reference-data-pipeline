# Azure Data Factory Pipeline Design

## Responsibility

Azure Data Factory is used as the orchestration layer. Large-scale data transformation and validation logic is kept in Databricks.

## High-level pipeline

```text
Trigger
   |
   v
Get / identify landing file
   |
   v
Run Databricks validation
   |
   v
Read validation result
   |
   +---- PASS ----> Staging ----> Delta load
   |
   +---- FAIL ----> Rejected
```

## Suggested activities

1. Trigger
2. Get Metadata
3. Databricks Notebook activity
4. If Condition
5. Copy/Move activity for valid files
6. Copy/Move activity for rejected files
7. Optional audit logging

## Validation result contract

Databricks can return a small control result:

```json
{
  "file_name": "instruments_valid.csv",
  "validation_status": "PASS",
  "duplicate_count": 0,
  "invalid_date_count": 0
}
```

For a rejected file:

```json
{
  "file_name": "instruments_duplicate.csv",
  "validation_status": "FAIL",
  "duplicate_count": 1,
  "invalid_date_count": 0
}
```

## Production enhancements

- retry policies
- audit tables
- pipeline run IDs
- correlation IDs
- alerting
- rejected-file monitoring
- idempotency checks
- quarantine retention policies
