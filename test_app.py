import pytest
from app import calculate_discount, authenticate_user

def test_calculate_discount_valid():
    assert calculate_discount(100.0, 20.0) == 80.0
    assert calculate_discount(50.0, 0.0) == 50.0

def test_calculate_discount_invalid():
    with pytest.raises(ValueError):
        calculate_discount(-10.0, 10.0)
    with pytest.raises(ValueError):
        calculate_discount(100.0, 110.0)

def test_authenticate_user():
    assert authenticate_user("arish", "admin") is True
    assert authenticate_user("guest", "viewer") is False
    assert authenticate_user("", "admin") is False