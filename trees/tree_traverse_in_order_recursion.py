from trees.Tree import Tree
from trees.Node import Node


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())

    traverse(tree.get_root())
    return visit_order


print(pre_order(tree))
