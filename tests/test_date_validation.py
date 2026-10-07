from datetime import datetime


def is_valid_date(value, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(value, date_format)
        return True
    except (TypeError, ValueError):
        return False


def test_valid_date():
    assert is_valid_date("2026-01-10") is True


def test_invalid_date_format():
    assert is_valid_date("10-01-2026") is False
