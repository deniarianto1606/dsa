# LIFO : Last In First Out
# implement stack using linked list
# first will become the Last In and First Out

# When Use Array, use push and pop to add and remove from last index, if not, we must shift the entire array

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, first=None, last=None, size=0):
        self.first = first
        self.last = last
        self.size = size

    def push(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = self.first
        else:
            new_node.next_node = self.first
            self.first = new_node
        self.size += 1
        return self.size

    # o(1) : remove the first directly
    # when last == first, set last to None
    def pop(self):
        if self.size == 0: return None
        deleted_node = self.first
        self.first = deleted_node.next_node
        if self.first is self.last:
            self.last = None
        self.size -= 1
        deleted_node.next_node = None
        return self.size


def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print()
    stack.pop()
    print()
    stack.pop()
    stack.pop()


test_push()
