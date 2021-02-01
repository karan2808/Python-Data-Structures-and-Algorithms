# Definition of a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.goLeft(root)
    
    def goLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self):
        topMost = self.stack[-1]
        self.stack.pop()
        # if right node, go to left most node of the right node
        if topMost.right != None:
            self.goLeft(topMost.right)
        return topMost.val
    
    def hasNext(self):
        return len(self.stack) > 0