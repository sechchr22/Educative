#!/usr/bin/python3

# Turning a binary tree into a Full binary tree
# References: 
# https://www.geeksforgeeks.org/binary-tree-data-structure/
# https://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/

# Given this tree:
#     1
#    / \
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \
#   0   3
#      / \
#     9   4

from collections import deque

class Node(object):
  # Class Node
  def __init__(self, value, left=None, right=None):
    # Node initialization
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    # String representation of a Node
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result

def fullBinaryTree(node):
  # Function to turn a tree into a Full tree
  if node is None:
    return

  if (node.left is not None and node.right is None):
    node.value = node.left.value
    buf = node.left
    node.left = node.left.left
    node.right = buf.right
  elif (node.right is not None and node.left is None):
    node.value = node.right.value
    buf = node.right
    node.right = node.right.right
    node.left = buf.left

  fullBinaryTree(node.left)
  fullBinaryTree(node.right)

# Creating a tree
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)

print("before")
print(tree)
print("after")
fullBinaryTree(tree)
print(tree)
