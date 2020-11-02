class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

class DepthFirstPostOrder:
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
            print(root_node.left.data)
        if root_node.right is not None:
            self.print_recursive(root_node.right)
            print(root_node.right.data)
    
    def print_recursive2(self, root_node):
        self.print_recursive(root_node)
        print(root_node.data)

    def print_recursive_return_array(self, root_node):
        results = []

        def post_order(node):
            if node is None:
                return None
            if node.left is not None:
                post_order(node.left)
                results.append(node.left.data)
            if node.right is not None:
                post_order(node.right)
                results.append(node.right.data)
            return results
        
        post_order(root_node)
        results.append(root_node.data)
        return results


def test_depth_first_search():
    binary = DepthFirstPostOrder()
    binary.push_recursive(10)
    binary.push_recursive(6)
    binary.push_recursive(3)
    binary.push_recursive(8)
    binary.push_recursive(15)
    binary.push_recursive(20)
    binary.print_recursive2(binary.root)
    print("=======")
    result = binary.print_recursive_return_array(binary.root)
    for i in range(len(result)):
        print(result[i])

test_depth_first_search()