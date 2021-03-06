from trees.Node import Node
from trees.Queue import Queue


class Tree():
    def __init__(self, value=None):
        if value is not None:
            self.set_root(value)
        else:
            self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert(self, new_value):
        if self.root == None:
            self.root = Node(new_value)
            return

        q = Queue()
        q.enq(self.get_root())

        while (True):
            node = q.deq()
            new_node = Node(new_value)

            if self.compare(node, new_node) == 0:
                node.set_value(new_node.get_value())
                break
            elif self.compare(node, new_node) == 1:
                if node.has_right_child():
                    q.enq(node.get_right_child())
                else:
                    node.set_right_child(new_node)
                    break
            else:
                if node.has_left_child():
                    q.enq(node.get_left_child())
                else:
                    node.set_left_child(new_node)
                    break

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        self._insert_with_recursion(self.get_root(), Node(value))

    def _insert_with_recursion(self, node, new_node):
        if self.compare(node, new_node) == 0:
            node.set_value(new_node.get_value())
        elif self.compare(node, new_node) == 1:
            if node.has_right_child():
                self._insert_with_recursion(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)
        else:
            if node.has_left_child():
                self._insert_with_recursion(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)

    """
        implement search
        """

    def search(self, value):
        if self.root == None:
            return None

        node = self.get_root()
        search_node = Node(value)

        while (True):
            if self.compare(node, search_node) == 0:
                return node
            elif self.compare(node, search_node) == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return None
            elif node.get_left_child():
                node = node.get_left_child()
            else:
                return None

    def delete(self, value):
        if self.root is None:
            return None

        node = self.get_root()
        delete_node = Node(value)
        previous_node = None
        node_left = False

        while self.compare(node, delete_node) != 0:
            previous_node = node
            if self.compare(node, delete_node) == -1:
                node = node.get_left_child()
                node_left = True
            else:
                node = node.get_right_child()
                node_left = False
            if node is None:
                return None

        if node.has_no_children():
            if self.compare(node, self.root) == 0:
                delete_node = self.root
                self.root = None
            elif node_left:
                delete_node = previous_node.get_left_child()
                previous_node.set_left_child(None)
            else:
                delete_node = previous_node.get_right_child()
                previous_node.set_right_child(None)

        elif node.has_only_right_child():
            if self.compare(node, self.root) == 0:
                delete_node = self.root
                self.root = node.get_right_child()
            elif node_left:
                delete_node = node
                previous_node.set_left_child(node.get_right_child())
            else:
                delete_node = node
                previous_node.set_right_child(node.get_right_child())

        elif node.has_only_left_child():
            if self.compare(node, self.root) == 0:
                delete_node = self.root
                self.root = node.get_left_child()
            elif node_left:
                delete_node = node
                previous_node.set_left_child(node.get_left_child())
            else:
                delete_node = node
                previous_node.set_right_child(node.get_left_child())
        else:
            successor = self.find_successor(node)
            if self.compare(node, self.root) == 0:
                delete_node = self.root
                self.root = successor
            elif node_left:
                delete_node = previous_node.get_left_child()
                previous_node.set_left_child(successor)
            else:
                delete_node = previous_node.get_right_child()
                previous_node.set_right_child(successor)
            successor.set_left_child(node.get_left_child())

        return delete_node

    def find_successor(self, node):
        successor = node
        previous_node = node
        current = node.get_right_child()

        while current is not None:
            previous_node = successor
            successor = current
            current = current.get_left_child()

        if successor != node.right:
            previous_node.set_left_child(successor.get_right_child())
            successor.set_right_child(node.get_right_child())

        return successor

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s
