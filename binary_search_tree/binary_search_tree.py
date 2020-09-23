class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

#     10
#   5      13
# 2   7  11  20
#   3
# BST typically will have 2 node (right and left)
# to insert we need check if value greater or lower and move to the right node
# if the node is null or None, create new node in that null node
# else we need to go to the right node until find the null or none node
# if the value exist, then return None
class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def push_rec(self, new_node, current):
        if new_node.data == current.data:
            return None
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
                return current.left
            else:
                return self.push_rec(new_node, current.left)
        else:
            if current.right is None:
                current.right = new_node
                return current.right
            else:
                return self.push_rec(new_node, current.right)

    def push_recursive(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            current = self.root
            return self.push_rec(new_node, current)

    def find_rec(self, data, current):

        if current.data == data:
            return True

        if data < current.data:
            if current.left is None:
                return None
            return self.find_rec(data, current.left)
        else:
            if current.right is None:
                return None
            return self.find_rec(data, current.right)

    def find_recursive(self, data):
        if self.root.data == data:
            return self.root.data
        else:
            current = self.root
            return self.find_rec(data, current)

    def push_with_loop(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            current = self.root
            while True:
                if data == current.data:
                    return None
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        return self.root
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return self.root
                    else:
                        current = current.right

    def find_with_loop(self, data):
        current = self.root
        while True:
            if current.data == data:
                return current.data
            else:
                if data < current.data:
                    if current.left is None:
                        return None
                    current = current.left
                else:
                    if current.right is None:
                        return None
                    current = current.right


def test():
    binary = BinarySearchTree()
    binary.push_recursive(10)
    binary.push_recursive(5)
    binary.push_recursive(7)
    binary.push_with_loop(2)
    binary.push_with_loop(3)
    binary.push_with_loop(2)
    print()


def test_find():
    binary = BinarySearchTree()
    binary.push_recursive(10)
    binary.push_recursive(5)
    binary.push_recursive(7)
    binary.push_with_loop(2)
    binary.push_with_loop(3)
    binary.find_with_loop(2)
    binary.find_recursive(7)
    binary.find_with_loop(1)
    print()

test_find()
test()