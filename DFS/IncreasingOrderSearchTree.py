class Solution:
    def __init__(self):
        self.current = None

    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        # set nodes left node as null and current nodes right node as node
        self.current.left = None
        self.current.right = node
        # set current node to node
        self.current = node
        # traverse through nodes right node
        self.inOrder(node.right)

    def increasingBST(self, root):
        ans = TreeNode(0)
        self.current = ans
        self.inOrder(root)
        return ans.right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    mySol = Solution()
    root = TreeNode(5)
    root.right = TreeNode(8)
    root.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    newRoot = mySol.increasingBST(root)
    while newRoot:
        print(newRoot.val)
        newRoot = newRoot.right

if __name__ == "__main__":
    main()
