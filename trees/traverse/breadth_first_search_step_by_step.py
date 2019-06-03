from trees.Node import Node
from trees.Tree import Tree
from trees.Queue import Queue

from collections import deque


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


visit_order = list()
q = Queue()

# start at the root node and add it to the queue
node = tree.get_root()
q.enq(node)
print(q)


# dequeue the next node in the queue.
# "visit" that node
# also add its children to the queue

node = q.deq()
visit_order.append(node)

if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)


# dequeue the next node (banana)
# visit it, and add its children (dates) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)


# dequeue the next node (cherry)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)


# dequeue the next node (dates)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)