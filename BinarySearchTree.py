class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curnode):
        if data < curnode.data:
            if curnode.left is None:
                curnode.left = Node(data)
            else:
                self._insert(data, curnode.left)
        if data > curnode.data:
            if curnode.right is None:
                curnode.right = Node(data)
            else:
                self._insert(data, curnode.right)

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def isbst(self):
        if self.root:
            issatisfied = self._isbst(self.root, self.root.data)
            if issatisfied is None:
                return True
            return False
        return True

    def _isbst(self, curnode, data):
        if curnode.left:
            if data > curnode.left.data:
                return self._isbst(curnode.left, curnode.left.data)
            else:
                return False
        if curnode.right:
            if data < curnode.right.data:
                return self._isbst(curnode.right, curnode.left.right)
            else:
                return False


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
# bst.insert(8)
# bst.insert(3)
# bst.insert(10)
# bst.insert(1)
# bst.insert(6)
# bst.insert(9)
# bst.insert(11)
# bst.inorder_print_tree()
# print(bst.find(10))
print(bst.isbst())