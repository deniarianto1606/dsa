class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

class DepthFirstInOrder:
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

    def print_recursive(self, root_node):
        if root_node is None:
            return None
        if root_node.left is not None:
            self.print_recursive(root_node.left)
        print(root_node.data)
        if root_node.right is not None:
            self.print_recursive(root_node.right)

    def print_recursive_return_array(self, root_node):
        results = []

        def post_order(node):
            if node is None:
                return None
            if node.left is not None:
                post_order(node.left)
            results.append(node.data)
            if node.right is not None:
                post_order(node.right)
            return results
        
        post_order(root_node)
        return results


def test_depth_first_search():
    binary = DepthFirstInOrder()
    binary.push_recursive(10)
    binary.push_recursive(6)
    binary.push_recursive(3)
    binary.push_recursive(8)
    binary.push_recursive(15)
    binary.push_recursive(20)
    binary.print_recursive(binary.root)
    print("=======")
    result = binary.print_recursive_return_array(binary.root)
    for i in range(len(result)):
        print(result[i])

test_depth_first_search()