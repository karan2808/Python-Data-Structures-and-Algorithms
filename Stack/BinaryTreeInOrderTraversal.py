class Solution:
    def inorderTraversal(self, root):

        result = []
        stack = []
        current = root

        # while current is not none or stack is not empty
        while current != None or len(stack) > 0:
            # push all the left nodes onto stack
            while current:
                stack.append(current)
                current = current.left

            # get the stack top, visit root node 
            current = stack.pop()
            result.append(current.val)

            # go to the right node and repeat
            current = current.right
        
        return result

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def main():
    mySol = Solution()
    root = TreeNode(1, None, TreeNode(2))
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    print("The inorder traversal of the BT is ") 
    print(mySol.inorderTraversal(root))

if __name__ == "__main__":
    main()