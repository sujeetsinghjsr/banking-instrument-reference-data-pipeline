# Business Requirement

## Objective

Build a data pipeline that receives instrument reference data from internal banking applications and validates incoming CSV files before the data is persisted into a Delta Lake platform.

## Functional requirements

1. Detect incoming files in the landing area.
2. Read the CSV file.
3. Validate duplicate records.
4. Validate date fields.
5. Retrieve configurable date rules from Azure SQL.
6. Reject files that fail validation.
7. Move rejected files to a rejected zone.
8. Move valid files to a staging zone.
9. Persist validated records as Delta.
10. Keep credentials outside source code.

A file is treated as an atomic processing unit for the mandatory validations in this example. If a mandatory validation fails, the complete file is rejected.
