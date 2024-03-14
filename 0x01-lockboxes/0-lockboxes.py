#!/usr/bin/python3
""""determine if each box can be opened"""


def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked = {0}

    # Initialize a queue to perform breadth-first search
    queue = [0]

    # Perform breadth-first search
    while queue:
        current_box = queue.pop(0)  # Get the current box

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and it's not unlocked yet
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)  # Unlock the box
                queue.append(key)  # Add the new box to the queue

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
