from trees.Tree import Tree


tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(5)  # insert duplicate
print(tree)

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5)  # insert duplicate
print(tree)

tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)