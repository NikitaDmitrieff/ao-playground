"""Tests for the calculator CLI interface."""
import subprocess
import sys


def test_cli_add_two_numbers():
    """Test adding two numbers from CLI."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'add', '5', '3'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '8' in result.stdout


def test_cli_add_multiple_numbers():
    """Test adding multiple numbers from CLI."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'add', '1', '2', '3', '4'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '10' in result.stdout


def test_cli_subtract():
    """Test subtracting numbers from CLI."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'subtract', '10', '3'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '7' in result.stdout


def test_cli_multiply():
    """Test multiplying numbers from CLI."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'multiply', '4', '5'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '20' in result.stdout


def test_cli_divide():
    """Test dividing numbers from CLI."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'divide', '20', '4'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '5' in result.stdout


def test_cli_help_shows_operations():
    """Test that help text shows available operations."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'add' in result.stdout
    assert 'subtract' in result.stdout
    assert 'multiply' in result.stdout
    assert 'divide' in result.stdout


def test_cli_invalid_operation_error():
    """Test that invalid operation returns error."""
    result = subprocess.run(
        [sys.executable, '-m', 'calculator', 'invalid', '5', '3'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
