class Node:
    def __init__(self, val):
        self.data = val
        self.rchild = None
        self.lchild = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not isinstance(val, Node):
            val = Node(val)

        if self.root is None:
            self.root = val

        else:
            self._insert(self.root, val)

    def _insert(self, curr, val):
        if val.data > curr.data:
            if curr.rchild is None:
                curr.rchild = val

            else:
                self._insert(curr.rchild, val)

        if val.data < curr.data:

            if curr.lchild is None:
                curr.lchild = val

            else:
                self._insert(curr.lchild, val)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.lchild)
            print(curr.data, end=" ")
            self._in_order(curr.rchild)

        if not curr:
            return " "

    def find_val(self, val):
        return self._find_val(self.root, val)

    def _find_val(self, curr, val):
        if curr:
            if val == curr.data:
                print("Value found in tree")

            elif val < curr.data:
                self._find_val(curr.lchild, val)

            else:
                self._find_val(curr.rchild, val)

        else:
            print("Value not found in tree")

        return ""


tree = BST()
tree.insert(15)
# print(tree.root.data)
tree.insert(20)
# print(tree.root.rchild.data)
tree.insert(10)
# print(tree.root.lchild.data)
tree.insert(35)
# print(tree.root.rchild.rchild.data)
tree.insert(25)
# print(tree.root.rchild.rchild.lchild.data)
tree.insert(50)
# print(tree.root.rchild.rchild.rchild.data)
print(tree.find_val(35))
print(tree.in_order())



