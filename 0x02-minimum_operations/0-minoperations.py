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

    # Initialize an array to store the min operations needed for each number
    dp = [0] * (n + 1)

    # Iterate from 2 to n to fill the dp array
    for i in range(2, n + 1):
        # If i is prime, it can only be formed by copying 1 character i times
        if dp[i] == 0:
            dp[i] = i
            for j in range(i * i, n + 1, i):
                dp[j] = dp[i] + dp[j // i]

    return dp[n]
