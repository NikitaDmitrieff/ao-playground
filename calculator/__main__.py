"""Command-line interface for the calculator."""
import argparse
import sys

from calculator import add, divide, multiply, subtract


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='A simple calculator for performing arithmetic operations'
    )

    subparsers = parser.add_subparsers(dest='operation', help='Available operations')

    # Add subcommands for each operation
    add_parser = subparsers.add_parser('add', help='Add numbers together')
    add_parser.add_argument('numbers', nargs='+', type=float, help='Numbers to add')

    subtract_parser = subparsers.add_parser('subtract', help='Subtract numbers')
    subtract_parser.add_argument('numbers', nargs='+', type=float, help='First number, then numbers to subtract')

    multiply_parser = subparsers.add_parser('multiply', help='Multiply numbers')
    multiply_parser.add_argument('numbers', nargs='+', type=float, help='Numbers to multiply')

    divide_parser = subparsers.add_parser('divide', help='Divide numbers')
    divide_parser.add_argument('numbers', nargs='+', type=float, help='First number, then numbers to divide by')

    args = parser.parse_args()

    if not args.operation:
        parser.print_help()
        sys.exit(1)

    try:
        if args.operation == 'add':
            result = add(*args.numbers)
        elif args.operation == 'subtract':
            result = subtract(*args.numbers)
        elif args.operation == 'multiply':
            result = multiply(*args.numbers)
        elif args.operation == 'divide':
            result = divide(*args.numbers)
        else:
            parser.print_help()
            sys.exit(1)

        print(result)
    except ZeroDivisionError:
        print('Error: Division by zero', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
