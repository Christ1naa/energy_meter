import pytest
from meter import calculate_bill

def test_normal_update():
    prev = {"day": 100, "night": 50}
    curr = {"day": 150, "night": 70}
    bill, _ = calculate_bill(prev, curr)
    assert bill['day_bill'] == 125
    assert bill['night_bill'] == 24

def test_night_rollback():
    prev = {"day": 100, "night": 90}
    curr = {"day": 150, "night": 10}
    bill, diffs = calculate_bill(prev, curr)
    assert "warning" in bill
    assert diffs['night'] == 10 - 90 + 80

def test_day_rollback():
    prev = {"day": 100, "night": 90}
    curr = {"day": 20, "night": 100}
    bill, diffs = calculate_bill(prev, curr)
    assert "warning" in bill
    assert diffs['day'] == 20 - 100 + 100

def test_both_rollback():
    prev = {"day": 100, "night": 90}
    curr = {"day": 20, "night": 10}
    bill, diffs = calculate_bill(prev, curr)
    assert diffs['day'] == 20 - 100 + 100
    assert diffs['night'] == 10 - 90 + 80
