IF NOT EXISTS (
    SELECT 1 FROM sys.schemas WHERE name = 'reference_data'
)
BEGIN
    EXEC('CREATE SCHEMA reference_data');
END;
