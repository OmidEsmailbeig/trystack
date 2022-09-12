from datetime import datetime

from trystack.util import now


def test_now():
    result = now()
    current_datetime = datetime.now()
    assert isinstance(result, datetime) is True
    assert hasattr(result, 'year') is True
    assert hasattr(result, 'month') is True
    assert hasattr(result, 'weekday') is True
    assert hasattr(result, 'day') is True
    assert hasattr(result, 'minute') is True
    assert hasattr(result, 'second') is True
    assert result.year == current_datetime.year
    assert result.month == current_datetime.month
    assert result.day == current_datetime.day
