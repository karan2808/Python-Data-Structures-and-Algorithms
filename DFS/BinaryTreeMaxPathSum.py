class Solution:
    def __init__(self):
        self.result = None

    def findMax(self, root):
        if root == None:
            return 0

        # find max for left and right node
        left = self.findMax(root.left)
        right = self.findMax(root.right)

        # can either go straight down i.e. from root to one of the children and downwards
        maxStraight = max(max(left, right) + root.val, root.val)

        # or can come to root from either of the child nodes and go to other child node
        maxCurved = max(left + right + root.val, maxStraight)

        # update the result
        self.result = max(self.result, maxCurved)

        # can only return max straight, since we're going upwards
        return maxStraight

    def maxPathSum(self, root):
        if root == None:
            return 0

        self.result = float('-inf')
        self.findMax(root)
        return self.result

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)
    mySol = Solution()
    print("The max path sum in the binary tree is " + str(mySol.maxPathSum(root)))


if __name__ == "__main__":
    main()
