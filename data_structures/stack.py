"""
Stacks are a data structure that implements a LIFO queue.
There are two major operations to preform on a Stack, push and pop.

When pushing an item onto a stack, that item becomes the first candidate for
removal during a pop operation.
"""

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()
