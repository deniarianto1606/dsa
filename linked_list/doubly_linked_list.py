# the different between singly linked list is doubly linked list has prev_node
class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def print(self):
        if self.head is None:
            print("None")
        else:
            temp = self.head
            text_to_print = ""
            while temp.next_node is not None:
                text_to_print += str(temp.data) + ", "
                temp = temp.next_node
            text_to_print += str(temp.data)
            print(text_to_print)

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

    # o(1) : because we can remove tail directly and change the tail to current tail prev_node
    def pop(self):
        if self.head is None:
            return None
        deleted_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            deleted_node.prev_node = None
        self.length -= 1
        return deleted_node

    # o(1) : because we can remove head directly
    # shifting in DLL is remove node from the beginning and set new head to old.next
    def shifting(self):
        if self.head is None:
            return None
        deleted_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
            deleted_node.next_node = None
        self.length -= 1
        return deleted_node

    # o(1) : because we can add new head directly
    def unshift(self, data):
        if self.head is None:
            return self.push(data)
        new_node = Node(data)
        new_node.next_node = self.head
        self.head.prev_node = new_node
        self.head = new_node
        return self.head

    # o(n) : because we need to traverse until index is same
    # o(1) : when the node is head or tail
    # optimization : change the search from tail when the index is > than median
    def get_in(self, index):
        if index < 0 or index >= self.length:
            return None
        mid = self.length // 2
        if index > mid:
            temp = self.tail
            counter = self.length - 1
        else:
            temp = self.head
            counter = 0
        while counter != index:
            if index > mid:
                temp = temp.prev_node
                counter -= 1
            else:
                temp = temp.next_node
                counter += 1
        return temp

    # set data at index (replacing data)
    # o(n) : because we need to traverse until index is same
    # optimization : change the search from tail when the index is > than median
    def set_in(self, data, index):
        temp = self.get_in(index)
        if temp is not None:
            temp.data = data
            return self.head
        return None


def test_set_in():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.push(99)
    doubly.set_in(88, 1)
    doubly.set_in(77, 0)
    doubly.set_in(5, 2)
    doubly.set_in(6, 3)
    doubly.print()


def test_get_in():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.push(99)
    doubly.push(8)
    doubly.push(9)
    doubly.push(10)
    print(doubly.get_in(5).data)


def test_unshift():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.push(99)
    doubly.unshift(8)
    doubly.unshift(9)
    doubly.unshift(10)
    doubly.print()


def test_shift():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.push(99)
    doubly.shifting()
    doubly.shifting()
    doubly.shifting()
    doubly.print()


def test_pop():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.push(99)
    doubly.pop()
    doubly.pop()
    doubly.pop()
    doubly.print()


def test_push():
    doubly = DoublyLinkedList()
    doubly.push(29)
    doubly.push(1)
    doubly.print()


test_set_in()
test_get_in()
test_unshift()
test_shift()
test_pop()
test_push()