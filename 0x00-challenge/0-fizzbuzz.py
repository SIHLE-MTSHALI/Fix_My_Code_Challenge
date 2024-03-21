#!/usr/bin/python3
"""
FizzBuzz Program: Prints numbers 1 to n, but for multiples of three prints
"Fizz" instead of the number, for the multiples of five prints "Buzz", and for
numbers which are multiples of both three and five prints "FizzBuzz".
"""

import sys

def fizzbuzz(n):
    """Implements the FizzBuzz logic."""
    if n < 1:
        return

    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz", end=' ')
        elif (i % 3) == 0:
            print("Fizz", end=' ')
        elif (i % 5) == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
    print()  # New line at the end of the sequence

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)

