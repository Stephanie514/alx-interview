#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
    n (int): The target number of H characters.

    Returns:
    int: The fewest number of operations needed, or 0 if impossible to achieve.
    """

    if n <= 1:
        return 0

    # Initialize the minimum number of operations
    operations = 0

    # Start with the smallest prime factor
    divisor = 2

    while n > 1:
        # Check if the current divisor divides n
        while n % divisor == 0:
            # If yes, update n and increment the operations
            n //= divisor
            operations += divisor

        # Move to the next divisor
        divisor += 1

    return operations
