# Architecture

## Logical architecture

The solution separates orchestration, processing, storage, metadata and secret management.

### Components

**Internal Banking Applications**  
Generate instrument reference data as CSV files.

**ADLS Gen2 - Landing**  
Receives source files without changing the original payload.

**Azure Data Factory**  
Orchestrates file detection, pipeline execution and Databricks processing.

**Azure Databricks**  
Performs distributed processing and data-quality validation using PySpark.

**Azure SQL**  
Stores configurable validation metadata such as date columns and expected formats.

**ADLS Gen2 - Staging**  
Stores files that successfully pass validation.

**ADLS Gen2 - Rejected**  
Stores files that fail validation for investigation and reprocessing.

**Delta Lake**  
Stores validated instrument reference data.

**Azure Key Vault**  
Provides secure management of secrets and sensitive configuration.

## Design principle

ADF = orchestration layer  
Databricks = processing and validation layer  
Azure SQL = configuration / metadata layer  
ADLS = storage layer  
Delta Lake = curated table layer
