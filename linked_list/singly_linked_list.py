class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList():
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    # push : insert last.
    # push o(1) : we can push directly to tail,
    # push o(n) : when we didn't have a tail.
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1
        return self.head

    # pop : remove last.
    # pop o(n) : we need to traverse until tail - 1 node
    # 9  3  1
    #    nt cn
    def pop(self):
        if self.head is None:
            return None
        current_node = self.head
        new_tail = self.head
        while current_node.next_node is not None:
            new_tail = current_node
            current_node = current_node.next_node
        self.tail = new_tail
        self.tail.next_node = None
        self.length -= 1
        return current_node

    # o(1) : just need move head pointer to next pointer
    def delete_first(self):
        if self.head is None:
            return None
        deleted_node = self.head
        self.head = self.head.next_node
        self.length -= 1
        if self.head is None:
            self.tail = self.head
        return deleted_node

    # o(1) : just need create new node and pointing next to head
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
        return self.head


def test_push():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    print()


def test_pop():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.pop()
    print()


def test_delete_first():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.delete_first()
    singly.delete_first()
    singly.delete_first()
    print()


def test_add_first():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.add_first(100)
    print()


test_push()
test_pop()
test_delete_first()
test_add_first()
