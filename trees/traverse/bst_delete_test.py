from trees.Tree import Tree

# delete no children root
tree = Tree()
tree.insert(5)
# print(tree)
node = tree.delete(5)
# print(tree)

if node.value == 5:
    print("\ndelete no children root test passed")


# delete no children left
tree = Tree()
tree.insert(10)
tree.insert(15)
tree.insert(5)
# print(tree)
node = tree.delete(5)
# print(tree)

if node.value == 5:
    print("\ndelete no children left test passed")


# delete no children right
tree = Tree()
tree.insert(10)
tree.insert(15)
tree.insert(5)
# print(tree)
node = tree.delete(15)
# print(tree)

if node.value == 15:
    print("\ndelete no children right test passed")


# delete node with left child
tree = Tree()
tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(12)
tree.insert(13)
print(tree)
node = tree.delete(15)
print(tree)

if node.value == 15 and tree.root.right.value == 12:
    print("\ndelete node with left child test passed")

