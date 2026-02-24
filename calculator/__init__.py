"""Calculator package."""


def add(*numbers):
    """Add all numbers together."""
    return sum(numbers)


def subtract(first, *rest):
    """Subtract all remaining numbers from the first."""
    result = first
    for num in rest:
        result -= num
    return result


def multiply(*numbers):
    """Multiply all numbers together."""
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(first, *rest):
    """Divide the first number by all remaining numbers."""
    result = first
    for num in rest:
        result /= num
    return result
