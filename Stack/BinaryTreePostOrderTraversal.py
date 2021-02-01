# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postorderTraversal(self, root):
        result = []
        stack = []

        current = root
        while current or len(stack) > 0:

            # push the current node onto stack and go to left node
            if current.left != None:
                stack.append(current)
                current = current.left
                stack[-1].left = None

            # push the current node onto stack and go to right node
            elif current.right != None:
                stack.append(current)
                current = current.right
                stack[-1].right = None

            # append the current nodes value to the stack, if there are elements on the stack, pop them
            else:
                result.append(current.val)
                if len(stack) > 0:
                    current = stack[-1]
                    stack.pop()
                else:
                    current = None

        return result


def main():
    mySol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)


if __name__ == "__main__":
    main()
