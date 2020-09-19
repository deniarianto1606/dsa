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
            return False
        current_node = self.head
        new_tail = self.head
        while current_node.next_node is not None:
            new_tail = current_node
            current_node = current_node.next_node
        self.tail = new_tail
        self.tail.next_node = None
        self.length -= 1
        return current_node


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


test_push()
test_pop()
