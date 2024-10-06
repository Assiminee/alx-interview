#!/usr/bin/python3
"""
Module containing pascal's triangle function
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of binomial
    coefficients, where the first and last elements of
    each row are 1, and each interior element is the sum of the
    two elements directly above it.

    :param n: An integer representing the number of rows in the triangle.
              Must be greater than 0.
    :return: A list of lists, where each inner list represents a row of
             Pascal's Triangle.
             Returns an empty list if n is 0 or less.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        new_row = [1]
        previous_row = triangle[-1]
        for j in range(1, i):
            new_row.append(previous_row[j - 1] + previous_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
