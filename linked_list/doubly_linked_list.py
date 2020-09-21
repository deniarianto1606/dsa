class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList():
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    # o(1) : because we can add directly from tail and set new tail to new node
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.length += 1
        return self.head


def test_push():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    print()


test_push()