# Lockbox Algorithm

## Overview
This project contains a Python implementation of the **Lockbox Algorithm**, which solves the problem of determining whether all boxes in a collection can be unlocked. Each box may contain keys that unlock other boxes, and the objective is to verify if all the boxes can be opened starting from the first unlocked box.

## Problem Description
You are given `n` number of locked boxes, where each box is numbered sequentially from `0` to `n - 1`. Every box may contain a list of keys, and each key can open a box corresponding to its number.

Your goal is to write a function `canUnlockAll(boxes)` that checks if you can unlock all the boxes starting from box `0`, which is initially unlocked. The function returns `True` if all the boxes can be opened, and `False` otherwise.

### Assumptions
- All keys are positive integers.
- There may be keys that do not match any box.
- The first box (`boxes[0]`) is always unlocked.

### Prototype
```python
def canUnlockAll(boxes):
    """ Determines if all boxes can be unlocked """
```

### Input
- boxes: A list of lists. Each element in boxes is a list of keys contained in that box.
### Output
- True if all boxes can be unlocked, otherwise False.

### Example
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [2], [3], [], [0]]
print(canUnlockAll(boxes))  # Output: False
```

### Algorithm
The function works as follows:

Start with the first unlocked box (box 0) and retrieve the keys inside it.
Use the keys to open other boxes.
Keep track of the opened boxes and continue retrieving new keys until no more boxes can be opened.
Return True if all boxes are opened, otherwise return False.

### Usage
You can run the function by importing it in a Python script or calling it in the Python interpreter.
```bash
$ python main.py
```
Where main contains the following code:
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # Output: False
```

