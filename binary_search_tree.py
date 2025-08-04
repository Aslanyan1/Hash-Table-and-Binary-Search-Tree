class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearcTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def search(self, data):
        current = self.root
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current.left
            else:
                current = current.right
        return None


    def __len__(self):
        def _count_nodes(node):
            if node is None:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        return _count_nodes(self.root)


bst = BinarySearcTree()
bst.insert(50)
bst.insert(30)
bst.insert(40)
bst.insert(70)
bst.insert(60)
print(bst.search(30))
print(len(bst))

