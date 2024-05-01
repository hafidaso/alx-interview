#!/usr/bin/python3
"""
Change comes from within
"""
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    Args:
        coins (list): A list of the values of the coins in possession.
        total (int): The desired total value.
    Returns:
        int: The fewest number of coins needed to meet the total.
        If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a list to store the minimum number of coins needed for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute the minimum number of coins needed for each value
    for val in range(1, total + 1):
        for coin in coins:
            if coin <= val:
                dp[val] = min(dp[val], dp[val - coin] + 1)

    # If the total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1
