import math


def power(a, b):
    """Return a raised to power b."""
    return a ** b


def modulo(a, b):
    """Return a mod b."""
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


def sqrt(a):
    """Return square root of a."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)


def absolute(a):
    """Return absolute value of a."""
    return abs(a)


def factorial(n):
    """Return n!"""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("Factorial requires an integer argument")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)
