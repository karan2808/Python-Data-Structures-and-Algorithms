class Solution:
    def __init__(self):
        self.nodeMap = {}

    def rob(self, root):
        if root == None:
            return 0

        if root in self.nodeMap.keys():
            return self.nodeMap[root]

        # calculate profit from root and grand children
        val = root.val
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)

        # calculate profit from roots children
        valChild = self.rob(root.left) + self.rob(root.right)

        # get max
        self.nodeMap[root] = max(val, valChild)
        return self.nodeMap[root]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    mySol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(2, None, TreeNode(3))
    root.right = TreeNode(3, None, TreeNode(1))
    print("Max amount of money the thief can rob is " + str(mySol.rob(root)))


if __name__ == "__main__":
    main()
