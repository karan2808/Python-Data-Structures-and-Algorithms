import sys
import math 

# Binary tree node has data, pointer to left child and pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
# This function traverses original binary tree and stores its node pointers in a list
def storeBSTNodes(root, nodes):
    if not root:
        return

    # do an inorder traversal and store the nodes
    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)


def buildTreeUtil(nodes, start, end):
    # base case
    if start > end:
        return None
    
    # get the middle element and make it root
    mid = (start + end) // 2
    node = nodes[mid]

    # using the index in inorder traversal, construct left and right sub trees
    node.left = buildTreeUtil(nodes, start, mid - 1)
    node.right = buildTreeUtil(nodes, mid + 1, end)

    return node

# convert to an unbalanced BST to a balanced BST
def buildTree(root):
    # store nodes of given BST in sorted order
    nodes = []
    storeBSTNodes(root, nodes)
    # constructs bst from nodes[]
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n - 1)

# function to do a preorder traversal of tree
def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data), end = "")
    preOrder(root.left)
    preOrder(root.right)

def main():
    # first we construct a skewed binary tree
    #          15
    #         /  \
    #        12   20
    #       /  \
    #      10   14
    #     /
    #    9
    #   /
    #  6
    # /
    # 3
    root = Node(15)
    root.left = Node(12)
    root.right = Node(20)
    root.left.left = Node(10)
    root.left.right = Node(14)
    root.left.left.left = Node(9)
    root.left.left.left.left = Node(6)
    root.left.left.left.left.left = Node(3)
    print("Preorder traversal of the imbalanced tree is ")
    preOrder(root)
    root = buildTree(root)
    print("\nPreorder traversal of the balanced tree is ")
    preOrder(root)

if __name__ == "__main__":
    main()