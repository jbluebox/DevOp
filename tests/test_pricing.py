import pytest

from app.pricing import apply_discount


def test_regular_discount():
    assert apply_discount(100.0, 20) == 80.0


def test_no_discount():
    assert apply_discount(59.90, 0) == 59.90


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(10.0, 120)
