# ADF Pipeline Parameters

Suggested parameters:

| Parameter | Example | Purpose |
|---|---|---|
| source_file_path | landing/instruments/ | Input location |
| source_file_name | instruments_valid.csv | Input file |
| staging_path | staging/instruments/ | Valid output |
| rejected_path | rejected/instruments/ | Invalid output |
| notebook_path | /Repos/... | Databricks notebook |
| environment | dev | Environment separation |

Use parameters instead of hard-coded environment-specific paths.
