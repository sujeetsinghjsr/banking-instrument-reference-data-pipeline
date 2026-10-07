CREATE TABLE reference_data.validation_date_rules
(
    rule_id INT IDENTITY(1,1) PRIMARY KEY,
    column_name VARCHAR(100) NOT NULL,
    expected_date_format VARCHAR(50) NOT NULL,
    is_active BIT NOT NULL DEFAULT 1,
    created_timestamp DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
