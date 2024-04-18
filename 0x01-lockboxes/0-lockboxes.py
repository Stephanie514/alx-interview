#!/usr/bin/python3
""" method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    stack = [0]
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)
