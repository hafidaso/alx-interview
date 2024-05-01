#!/usr/bin/python3
"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in possession.
        total (int): The desired total value.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, returns -1.

    This implementation uses dynamic programming to solve the coin change problem.
    The basic idea is to build a list (dp) that stores the minimum number of coins
    needed to make each value from 0 to the target total. We initialize dp[0] to 0,
    since no coins are needed to make a total of 0. For every other value 'i' from
    1 to the target total, we check each coin denomination and update dp[i] with
    the minimum of its current value and dp[i - coin] + 1. This means that the
    minimum number of coins needed for 'i' is either the current value in dp[i]
    or dp[i - coin] + 1 (the minimum number of coins needed for 'i - coin' plus
    one coin of the current denomination).

    After computing the minimum number of coins needed for each value, we check
    the value in dp[total]. If it's not infinity, it represents the minimum number
    of coins needed to make the total. Otherwise, if it's infinity, it means the
    total cannot be met by any combination of coins, so we return -1.

    This solution has a time complexity of O(n * m), where n is the total value,
    and m is the number of coin denominations. It uses dynamic programming to
    avoid redundant computations and find the optimal solution efficiently.
    """

    # Base case: If the total is 0 or negative, no coins are needed
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each value
    dp = [0]
    for _ in range(total):
        dp.append(float("inf"))

    # Iterate over each coin denomination
    for coin in coins:
        # For each value 'i' from 'coin' to 'total'
        for i in range(coin, total + 1):
            # Update dp[i] with the minimum of its current value and dp[i - coin] + 1
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total cannot be met, return -1
    return dp[total] if dp[total] != float("inf") else -1
