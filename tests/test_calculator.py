import pytest

from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_adds_two_positive_numbers(self):
        assert add(2, 3) == 5

    def test_adds_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_adds_zero(self):
        assert add(5, 0) == 5

    def test_adds_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtracts_two_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtracts_resulting_in_negative(self):
        assert subtract(3, 5) == -2

    def test_subtracts_zero(self):
        assert subtract(5, 0) == 5

    def test_subtracts_floats(self):
        assert subtract(5.5, 2.5) == 3.0


class TestMultiply:
    def test_multiplies_two_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiplies_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiplies_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_multiplies_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_divides_two_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divides_resulting_in_float(self):
        assert divide(7, 2) == 3.5

    def test_divides_negative_numbers(self):
        assert divide(-10, 2) == -5.0

    def test_divides_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divides_floats(self):
        assert divide(7.5, 2.5) == 3.0
