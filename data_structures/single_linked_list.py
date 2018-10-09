"""
A Singly-Linked List is a sequence of objects that point to the next item in
the list but have no back references to previous items in the list.
"""


class ListElement:
    def __init__(self, data):
        self.next_item = None
        self.data = data

    def append(self, data):
        self.last().next_item = ListElement(data)

    def last(self):
        if not self.next_item:
            return self
        else:
            return self.next_item.last()
