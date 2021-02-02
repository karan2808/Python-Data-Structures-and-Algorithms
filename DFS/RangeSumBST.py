class Solution:
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        rangeSum = 0
        # use node value only if its within range
        if root.val >= low and root.val <= high:
            rangeSum = root.val
        return rangeSum + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    mySol = Solution()
    print("The range sum for the given tree is " + str(mySol.rangeSumBST(root, 6, 9)))

if __name__ == "__main__":
    main()