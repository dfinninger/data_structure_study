import pytest

from data_structures import array

def test_static_array():
    arr = array.StaticArray(str, 3)
    arr.add("foo")
    arr.add("bar")
    arr.add("baz")

    assert "foo" == arr.get(0)
    assert "bar" == arr.get(1)
    assert "baz" == arr.get(2)

    with pytest.raises(array.MaxArraySizeError):
        arr.add("quux")

    arr.remove(0)
    assert "bar" == arr.get(0)
    assert "baz" == arr.get(1)
