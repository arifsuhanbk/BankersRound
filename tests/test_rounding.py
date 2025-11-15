import pytest
from bankers_round.rounding import bankers_round

def test_bankers_round_basic():
    assert bankers_round(1.234) == 1.23
    assert bankers_round(1.235) == 1.24


def test_bankers_round_half_even_even_case():
    # 1.005 → tie → goes to even (1.00)
    assert bankers_round(1.005) == 1.00

    # 2.015 → tie → goes to even (2.02)
    assert bankers_round(2.015) == 2.02


def test_bankers_round_half_even_odd_case():
    # 1.015 → 1.02 (because 2 is even)
    assert bankers_round(1.015) == 1.02

    # 1.025 → 1.02 (2 is even)
    assert bankers_round(1.025) == 1.02


# @pytest.mark.parametrize("value, expected", [
#     (2.5, 2.0),   # even
#     (3.5, 4.0),   # even
#     (4.5, 4.0),   # even
#     (5.5, 6.0),   # even
# ])
# def test_bankers_round_whole_numbers(value, expected):
#     assert bankers_round(value) == expected
