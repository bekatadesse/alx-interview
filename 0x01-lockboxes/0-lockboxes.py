#!/usr/bin/python3
"""Module 0-lockboxes"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes
    can be opened.
    """
    if boxes is None:
        return False
    if len(boxes) == 1:
        return True

    visited = set()

    visited.add(0)

    stack = []
    stack.append(0)

    while stack:
        keys = boxes[stack.pop()]
        for key in keys:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    return len(boxes) == len(visited)
