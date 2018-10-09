"""
A Queue is a collection of elements that allow for insertion and removal from the group.
When an item is removed from the group, it is the item with the oldest insertion time.
"""

class Queue:
    def __init__(self):
        self._queue = []

    def push(self, item):
        self._queue.append(item)

    def pop(self):
        return self._queue.pop(0)
