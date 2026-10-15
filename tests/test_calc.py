from src.calc import clamp


def test_upper_bound():
    assert clamp(6, 1, 5) == 5
