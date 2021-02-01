class Solution:
    def preorderTraversal(self, root):
        preorder = []
        stack = []

        if root == None:
            return preorder
        
        stack.append(root)

        # while there are elements on the stack
        while len(stack):  

            # get current node from top of the stack
            root = stack[-1]
            stack.pop()
            # append the node value to preorder array
            preorder.append(root.val)

            # push nodes right node on the stack so it gets visited after left
            if root.right != None:
                stack.append(root.right)
            
            if root.left != None:
                stack.append(root.left)
        
        return preorder

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
    print("The preorder traversal of the BT is ") 
    print(mySol.preorderTraversal(root))

if __name__ == "__main__":
    main()