class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, current, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, current, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.right

    def rebalance(self, node):
        if node.parent is None:
            return
        if node.parent.color == 'black':
            return
        # From here, we know parent's color is red
        # Case 3
        if pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            self.rebalance(grandparent(node))


    def search(self, find_val):
        return False
