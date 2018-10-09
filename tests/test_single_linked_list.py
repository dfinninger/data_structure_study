import pytest

from data_structures.single_linked_list import ListElement


def test_singly_linked_list():
    first = ListElement("foo")
    first.append("bar")
    first.append("baz")

    assert "bar" == first.next_item.data
    assert "baz" == first.next_item.next_item.data

    assert "baz" == first.last().data
