# Data Quality Rules

## Rule 1 - Duplicate rows

The complete record is checked for duplicates.

If duplicate rows are detected, the source file is rejected.

## Rule 2 - Date format

Configured date fields are validated against metadata.

| Column | Expected format |
|---|---|
| trade_date | yyyy-MM-dd |
| maturity_date | yyyy-MM-dd |
| settlement_date | yyyy-MM-dd |

## Rule 3 - File routing

| Validation result | Destination |
|---|---|
| PASS | Staging |
| FAIL | Rejected |

## Future rules

The framework can be extended with mandatory-field checks, allowed-value checks, reference-data checks, ISIN validation, currency validation, schema validation and null thresholds.
