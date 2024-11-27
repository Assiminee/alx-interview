#!/usr/bin/python3
"""
Contains makeChange method
"""
from functools import lru_cache


def makeChange(coins, total):
    """
    Given a pile of 'coins' of different values,
    determines the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    if len(coins) < 1 or min(coins) > total:
        return -1

    possibilities = []
    coins = sorted(coins, reverse=True)
    while len(coins) > 0:
        change = makeChangeHelper(tuple(coins), total)
        coins = coins[1:]
        if change == -1 or change in possibilities:
            continue
        possibilities.append(change)

    if len(possibilities) > 0:
        return min(possibilities)

    return -1


def makeChangeHelper(coins, total):
    """
    Helper method
    """
    change = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            change += 1

    if total != 0:
        return -1

    return change
