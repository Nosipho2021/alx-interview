#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):

    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes with keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if key < n and key not in visited:
                    queue.append(key)

    return len(visited) == n


if __name__ == "__main__":
    boxes = [[1, 2], [3], [], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 2], [3], [0, 1], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 2], [3], [0, 1], [4]]
    print(canUnlockAll(boxes))
