# Pascal's Triangle

This project implements **Pascal's Triangle** in Python, a famous mathematical structure that forms a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it, starting with 1 at the top.

## Description

The **Pascal's Triangle** function generates the triangle up to the given number of rows `n`. The function will return a list of lists, where each inner list represents a row in the triangle.

Pascal's Triangle is not only useful in combinatorics but also has applications in algebra, probability, and various other mathematical domains.

### Example:

For `n = 5`, the function will return:

```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```


## Usage

To use this function, simply call `pascal_triangle(n)` where `n` is the number of rows you want to generate.

```python
from pascal_triangle import pascal_triangle

# Generate Pascal's Triangle with 5 rows
triangle = pascal_triangle(5)
print(triangle)
```

## Parameters:
- n: (int) The number of rows to generate. Should be greater than 0.

## Return Value:
- A list of lists where each list represents a row in Pascal's Triangle. If n is 0 or less, an empty list is returned.

