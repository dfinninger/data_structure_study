"""
Doubly Linked Lists have references to the next and previous elements
"""


class ListElement:
    def __init__(self, data, prev_item=None, next_item=None):
        self.data = data
        self.next_item = prev_item
        self.prev_item = next_item

    def append(self, data):
        if self.next_item:
            self.next_item.append(data)
        else:
            self.next_item = ListElement(data, prev_item=self)

    def prepend(self, data):
        if self.prev_item:
            self.prev_item.append(data)
        else:
            self.prev_item = ListElement(data, next_item=self)
