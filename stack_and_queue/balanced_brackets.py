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

    def pop(self):
        if self.size == 0: return None
        deleted_node = self.first
        self.first = deleted_node.next_node
        if self.first is self.last:
            self.last = None
        self.size -= 1
        deleted_node.next_node = None
        return self.size

    def get_last(self):
        if self.first is None:
            return None
        return self.first.data


# read string one by one by char value per index
# if stack size is 0, then push and continue
# if stack.get_last (last in) equal open and the string is its pair, then pop the stack
# else push
def isBalanced(s):
    # for i in range(len(s)):
    #     print(str(ord(s[i])))
    buka_kurawal = '{'
    buka_siku = '['
    buka_kurung = '('
    tutup_kurawal = '}'
    tutup_siku = ']'
    tutup_kurung = ')'

    stack = Stack()
    for i in range(len(s)):
        if stack.size == 0:
            stack.push(s[i])
            continue
        if stack.get_last() == buka_kurawal and s[i] == tutup_kurawal:
            stack.pop()
            continue
        elif stack.get_last() == buka_siku and s[i] == tutup_siku:
            stack.pop()
            continue
        elif stack.get_last() == buka_kurung and s[i] == tutup_kurung:
            stack.pop()
            continue
        else:
            stack.push(s[i])
    if stack.size == 0:
        return "YES"
    else:
        return "NO"


def test():
    print(isBalanced("{(([])[])[]}"))

test()