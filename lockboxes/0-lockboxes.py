#!/usr/bin/env python3
"""Lockboxes challenge"""


def canUnlockAll(boxes):
    opened = set([0])
    keys = boxes[0]
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            for box in boxes[key]:
                keys.append(box)

    print(opened)
    return len(opened) == len(boxes)
