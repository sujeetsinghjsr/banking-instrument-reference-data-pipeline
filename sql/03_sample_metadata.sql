INSERT INTO reference_data.validation_date_rules
(
    column_name,
    expected_date_format,
    is_active
)
VALUES
('trade_date', 'yyyy-MM-dd', 1),
('maturity_date', 'yyyy-MM-dd', 1),
('settlement_date', 'yyyy-MM-dd', 1);
