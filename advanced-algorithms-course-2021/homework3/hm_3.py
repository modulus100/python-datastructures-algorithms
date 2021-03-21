import math


class Node:
    def __init__(self, key: int, right=None, left=None):
        self.key = key
        self.right = right
        self.left = left


class Tree:
    def __init__(self, root: Node):
        self.root = root


def distance_array(a: list, b: list):
    c = math.inf
    for i in range(len(a)):
        for j in range(len(b)):
            d = abs(a[i] - b[j])
            c = min(c, d)
    return c


def distance_num_bst(p: int, x: Node):
    if x is None:
        return math.inf
    if p == x.key:
        return 0
    d = abs(p - x.key)
    if p < x.key:
        return min(d, distance_num_bst(p, x.left))
    return min(d, distance_num_bst(p, x.right))


def distance_bst(x: Node, y: Node):
    if x is None or y is None:
        return math.inf
    if x.key == y.key:
        return 0

    c = abs(x.key - y.key)
    c = min(c, distance_bst(x.left, y.left))
    c = min(c, distance_bst(x.right, y.right))

    if x.key < y.key:
        c = min(c, distance_bst(x.right, y.left))
        c = min(c, distance_num_bst(x.key, y.left))
        c = min(c, distance_num_bst(y.key, x.right))
    else:
        c = min(c, distance_bst(x.left, y.right))
        c = min(c, distance_num_bst(x.key, y.right))
        c = min(c, distance_num_bst(y.key, x.left))
    return c


a = [6, 5]
b = [2, 8]

# print("distance array: " + str(distance_array(a, b)))

root_a = Node(27)
root_a.left = Node(16)
root_a.right = Node(35)
root_a.left.left = Node(10)
root_a.left.right = Node(22)
root_a.right.left = Node(31)
root_a.right.right = Node(45)

root_b = Node(29)
root_b.left = Node(19)
root_b.right = Node(42)
root_b.left.left = Node(13)
root_b.left.right = Node(25)
root_b.right.left = Node(38)
root_b.right.right = Node(54)

# print("distance point tree: " + str(distance_num_bst(100, root_a)))
print("distance tree tree: " + str(distance_bst(root_a, root_b)))


def distance_array_sorted(a: list, b: list):
    min_diff = math.inf
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])

        if diff == 0:
            return 0

        if min_diff > diff:
            min_diff = diff

        if a[i] > b[j]:
            j += 1
        else:
            i += 1

    return min_diff


a = [10, 16, 22, 27, 31, 35, 45]
b = [13, 19, 25, 29, 38, 42, 54]

print("distance sorted lists: " + str(distance_array_sorted(a, b)))

