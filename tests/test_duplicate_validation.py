def has_duplicates(records):
    return len(records) != len({tuple(sorted(record.items())) for record in records})


def test_duplicate_records_are_detected():
    records = [
        {"instrument_id": "INS001", "currency": "USD"},
        {"instrument_id": "INS001", "currency": "USD"},
    ]
    assert has_duplicates(records) is True


def test_unique_records_pass():
    records = [
        {"instrument_id": "INS001", "currency": "USD"},
        {"instrument_id": "INS002", "currency": "GBP"},
    ]
    assert has_duplicates(records) is False
