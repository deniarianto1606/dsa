class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

class DepthFirstPreOrder:
    def __init__(self, root=None):
        self.root = root

    # BFS push using recursive, loop version had already implement in BST package
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

    def print_recursive(self, n):
        if self.root is None:
            return None
        print(n.data)
        if n.left is not None:
            self.print_recursive(n.left)
        if n.right is not None:
            self.print_recursive(n.right)
    
    def print_recursive_return_array(self):
        visited = []
        current = self.root
        def get_visited(c):
            if c is None:
                return None
            visited.append(c)
            if c.left is not None:
                get_visited(c.left)
            if c.right is not None:
                get_visited(c.right)
        get_visited(current)
        return visited
    
def test_depth_first_search():
    binary = DepthFirstPreOrder()
    binary.push_recursive(10)
    binary.push_recursive(6)
    binary.push_recursive(3)
    binary.push_recursive(8)
    binary.push_recursive(15)
    binary.push_recursive(20)
    binary.print_recursive(binary.root)
    print("=======")
    result = binary.print_recursive_return_array()
    for i in range(len(result)):
        print(result[i].data)

test_depth_first_search()
