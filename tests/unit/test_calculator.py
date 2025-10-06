from src.calculator import add, subtract

class TestCalculator:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_subtract_negative_numbers(self):
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2
from src.calculator import power, square_root

class TestAdvancedOperations:
    def test_power_positive_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_square_root_positive_numbers(self):
        assert square_root(4) == 2
        assert square_root(9) == 3

    def test_square_root_negative_raises_error(self):
        import pytest
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-4)