import pytest

from data_structures.queue import Queue

def test_queue():
    queue = Queue()
    queue.push("foo")
    queue.push("bar")
    queue.push("baz")

    assert "foo" == queue.pop()
    assert "bar" == queue.pop()
    assert "baz" == queue.pop()

