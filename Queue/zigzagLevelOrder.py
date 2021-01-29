# definition of a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        # use a queue for bfs
        queue = []
        # push the root onto the queue
        queue.append(root)
        # keep a flag to indicate traversal direction
        flag = True
        while len(queue) > 0:
            # get the queue size
            sz = len(queue)
            # store the current level
            currentLevel = []
            # for all elements in the queue
            for i in range(sz):
                currentNode = queue.pop(0)
                # push to the current level
                currentLevel.append(currentNode.val)
                # if current node has left or right add to queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            # if the flag is set, reverse order of elements
            if flag:
                # reverse the current level
                currentLevel.reverse()
                result.append(currentLevel)
                flag = False
            else:
                # append as it is
                result.append(currentLevel)
                flag = True
        return result

def printRes(levels):
    for level in levels:
        result = ""
        for val in level:
            result += str(val) + " "
        print(result)

def main():
    mySol = Solution()
    root = TreeNode(5, TreeNode(3), TreeNode(6))
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.right.right = TreeNode(8, TreeNode(7), TreeNode(8))
    root.right.right.left.left = TreeNode(6)
    root.right.right.left.right = TreeNode(8)
    result = mySol.zigzagLevelOrder(root)
    printRes(result)

if __name__ == "__main__":
    main()