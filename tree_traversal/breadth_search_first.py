class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


class BinarySearchTree:
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

    def breadth_first_search_print(self, root):
        if root.left is not None:
            print(root.left.data)
        if root.right is not None:
            print(root.right.data)
            
        if root.left is not None:
            self.breadth_first_search_print(root.left)
        if root.right is not None:
            self.breadth_first_search_print(root.right)

    def breadth_first_search(self):
        if self.root is None:
            return None
        print(self.root.data)
        self.breadth_first_search_print(self.root)

    def breadth_first_search_loop(self):
        if self.root is None:
            return None
        
        bfs = []
        bfs.append(self.root)
        while len(bfs) != 0:
            print(bfs[0].data)
            if bfs[0].left is not None:
                bfs.append(bfs[0].left)
            if bfs[0].right is not None:
                bfs.append(bfs[0].right)
            bfs.pop(0)
            

def test_breadth_first_search():
    binary = BinarySearchTree()
    binary.push_recursive(10)
    binary.push_recursive(6)
    binary.push_recursive(3)
    binary.push_recursive(8)
    binary.push_recursive(15)
    binary.push_recursive(20)
    binary.breadth_first_search()
    print("=======")
    binary.breadth_first_search_loop()

test_breadth_first_search()
