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
