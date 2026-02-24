import pytest
from calculator import power, modulo, sqrt, absolute, factorial


class TestPower:
    def test_power_basic(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25

    def test_power_float_base(self):
        assert power(2.5, 2) == 6.25


class TestModulo:
    def test_modulo_basic(self):
        assert modulo(10, 3) == 1

    def test_modulo_zero_remainder(self):
        assert modulo(10, 5) == 0

    def test_modulo_negative_numbers(self):
        assert modulo(-10, 3) == 2

    def test_modulo_division_by_zero(self):
        with pytest.raises(ValueError):
            modulo(10, 0)


class TestSqrt:
    def test_sqrt_perfect_square(self):
        assert sqrt(4) == 2

    def test_sqrt_non_perfect_square(self):
        result = sqrt(2)
        assert abs(result - 1.414213562) < 0.001

    def test_sqrt_zero(self):
        assert sqrt(0) == 0

    def test_sqrt_one(self):
        assert sqrt(1) == 1

    def test_sqrt_negative_number(self):
        with pytest.raises(ValueError):
            sqrt(-1)


class TestAbsolute:
    def test_absolute_positive(self):
        assert absolute(5) == 5

    def test_absolute_negative(self):
        assert absolute(-5) == 5

    def test_absolute_zero(self):
        assert absolute(0) == 0

    def test_absolute_float(self):
        assert absolute(-3.14) == 3.14


class TestFactorial:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_basic(self):
        assert factorial(5) == 120

    def test_factorial_larger(self):
        assert factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_float(self):
        with pytest.raises(ValueError):
            factorial(5.5)
