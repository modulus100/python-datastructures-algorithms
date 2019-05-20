
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        temp_node = self.head
        self.head = Node(value)
        self.head.next = temp_node

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)


test_list = LinkedList()
# test_list.prepend(1)
# test_list.prepend(2)
# test_list.prepend(3)

test_list.append(4)
test_list.append(5)
test_list.append(6)
test_list.append(7)

print(test_list.head.value)
print(test_list.head.next.value)
print(test_list.head.next.next.value)
