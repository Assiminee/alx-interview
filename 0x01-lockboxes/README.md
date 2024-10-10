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
