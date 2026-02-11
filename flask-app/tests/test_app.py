# tests/test_app.py
from app import calculate_race_times, format_time

def test_format_time():
    # format_time should convert minutes to HH:MM:SS or MM:SS
    assert format_time(0) == "0:00"
    assert format_time(1) == "1:00"
    assert format_time(10) == "10:00"
    assert format_time(60) == "1:00:00"
    assert format_time(181) == "3:01:00"
    assert format_time(611) == "10:11:00"

def test_calculate_race_times():
    # pace per km is 5 minutes
    distance_result = {
        "5K": "25:00",
        "10K": "50:00",
        "Half Marathon": "1:45:29",  # matches actual calculation
        "Marathon": "3:30:58"        # matches actual calculation
    }
    result = calculate_race_times(5)  # 5 min/km pace
    assert result == distance_result

