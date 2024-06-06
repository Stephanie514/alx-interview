#!/usr/bin/python3
"""
0-making_change.py

This module provides a function to determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount of money.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    coins.sort()

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        if coin > total:
            break
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(
                    min_coins[amount],
                    min_coins[amount - coin] + 1
                )
            else:
                break

    return min_coins[total] if min_coins[total] != float('inf') else -1
