class MaxArraySizeError(Exception):
    """This array is at its maximum value"""
    pass

class InvalidArrayTypeError(Exception):
    """Invalid type inserted into an Array that is not the initial type"""
    pass

class StaticArray:
    """Defines an Array type that serves as a collection of a multiple instances of a single type"""
    def __init__(self, arr_type: type, max_size: int):
        """
        Args:
            arr_type: is a type, something like `str` or `type("foo")`
            max_size: the size of the array, the number of elements allowed
        """
        self.type = arr_type
        self.max_size = max_size
        self._list = []  # Major cop-out for the moment

    def add(self, item):
        """
        Add item to array

        Args:
            item: element to add to the array
        """
        if not len(self._list) < self.max_size:
            raise MaxArraySizeError

        if not isinstance(item, self.type):
            raise InvalidArrayTypeError

        self._list.append(item)

    def get(self, index):
        """Return the element found at index"""
        return self._list[index]

    def remove(self, index):
        """Delete the element at index"""
        del self._list[index]

