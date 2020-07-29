class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

        self.size += 1

    def remove_head(self):
        head = self.head

        if self.head is None and self.tail is None:
            return None

        if self.head.get_next() is None:
            self.head = None
            self.tail = None
            self.size = 0
            return head.get_value()

        self.head = self.head.get_next()
        self.size -= 1
        return head.get_value()

    def remove_tail(self):
        current = self.head
        tail = self.tail.get_value()

        if self.head is None and self.tail is None:
            return None

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return tail

        while current.get_next() is not self.tail and current.get_next() is not None:
            current = current.get_next()

        self.tail = current
        return tail

    def contains(self, value):
        current = self.head

        while current is not None:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def get_max(self):
        if self.head is None:
            return None

        max_value = 0
        current = self.head

        while current is not None:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()

        return max_value