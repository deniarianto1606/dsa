# FIFO : First In First Out
# implement stack using linked list
# add from size
# remove from first

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue2:
    def __init__(self, first=None, last=None, size=0):
        self.first = first
        self.last = last
        self.size = size

    def enqueue(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next_node = new_node
            self.last = new_node
        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return None
        if self.first.next_node is None:
            self.first = None
            self.last = None
        else:
            deleted = self.first
            self.first = self.first.next_node
            deleted.next_node = None
        self.size -= 1
        return self.size


def test_queue_push():
    queue = Queue2()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

test_queue_push()