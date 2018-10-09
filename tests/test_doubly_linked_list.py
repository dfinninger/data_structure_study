import pytest

from data_structures.doubly_linked_list import ListElement


def test_doubly_linked_list():
    middle = ListElement("bar")
    middle.prepend("foo")
    middle.append("baz")

    assert "foo" == middle.prev_item.data
    assert "baz" == middle.next_item.data
