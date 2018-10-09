import pytest

from data_structures.stack import Stack

def test_stack():
    stack = Stack()
    stack.push("foo")
    stack.push("bar")
    stack.push("baz")

    assert "baz" == stack.pop()
    assert "bar" == stack.pop()
    assert "foo" == stack.pop()
