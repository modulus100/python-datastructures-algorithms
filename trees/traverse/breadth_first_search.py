from trees.Node import Node
from trees.Tree import Tree
from trees.Queue import Queue


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def bfs(tree):
    q = Queue()
    visit_order = list()

    node = tree.get_root()
    q.enq(node)

    while len(q) > 0:
        node = q.deq()
        visit_order.append(node)

        if node.has_left_child():
            q.enq(node.get_left_child())

        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order


print(bfs(tree))
