#!/usr/bin/python3
"""
Contains function definition of minOperations(n)
"""
import math


def sumFactors(n):
    """
    Calculates sum of factors of n
    :param n: an integer
    :return: number of factors of n
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return sum(factors)


def minOperations(n):
    """
    Calculates minimum operations to reach n
    :param n: an integer
    :return: minimum operations to reach n
    """
    if n <= 1:
        return 0

    if n in [2, 3, 4]:
        return n

    return sumFactors(n)
