from trees.Node import Node


class Tree(object):
    def __init__(self, value):
        if isinstance(value, Node):
            self.root = value
        else:
            self.root = Node(value)

    def get_root(self):
        return self.root
