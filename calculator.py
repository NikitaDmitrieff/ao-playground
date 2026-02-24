def add(a: int | float, b: int | float) -> float:
    """Add two numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b as a float.
    """
    return a + b


def subtract(a: int | float, b: int | float) -> float:
    """Subtract two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference (a - b) as a float.
    """
    return a - b


def multiply(a: int | float, b: int | float) -> float:
    """Multiply two numbers.

    Args:
        a: The first number to multiply.
        b: The second number to multiply.

    Returns:
        The product of a and b as a float.
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide two numbers.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient (a / b) as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
