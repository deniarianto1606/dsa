class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList():
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def print(self):
        text_to_print = ""
        temp = self.head
        while temp.next_node is not None:
            text_to_print += str(temp.data) + ", "
            temp = temp.next_node
        text_to_print += str(temp.data)
        print(text_to_print)

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

    # o(n): we need to traverse until position of index
    def get_in(self, index):
        counter = 0
        if index > self.length or index < 0:
            return None
        temp = self.head
        while counter != index:
            temp = temp.next_node
            counter += 1
        return temp

    # o(n): we need to traverse until position of index
    # set_in will replace data in index n
    def set_in(self, data, index):
        temp = self.get_in(index)
        temp.data = data
        return self.head

    # o(n): we need to traverse until position of index
    # set_in will replace data in index n
    # need temp and current node to change the pointer
    # insert_in will shift current index to become next node for new data
    def insert_in(self, data, index):
        if index > self.length or index < 0:
            return None
        self.length += 1
        if index == 0: return self.add_first(data)
        if self.length == index: return self.push(data)
        counter = 0
        temp = self.head
        current = temp
        while counter != index:
            current = temp
            temp = temp.next_node
            counter += 1
        new_node = Node(data)
        current.next_node = new_node
        new_node.next_node = temp
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


def test_get_in():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.get_in(-1)

def test_set_in():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.set_in(100, 1)
    #singly.print()


def test_insert_in():
    singly = SinglyLinkedList()
    singly.push(9)
    singly.push(1)
    singly.push(3)
    singly.insert_in(100, 2)
    singly.insert_in(99, 0)
    singly.insert_in(77, 5)
    singly.print()

test_push()
test_pop()
test_delete_first()
test_add_first()
test_get_in()
test_set_in()
test_insert_in()