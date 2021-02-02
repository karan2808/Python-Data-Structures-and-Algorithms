# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if node == None:
            return None

        # make a set to store visited nodes
        visitedSet = set()
        # use a hasmap to map existing nodes to new ones
        hashMap = {}
        
        # dfs function
        def dfs(node, visitedSet, hashMap):
            # add the current node to visited set
            visitedSet.add(node)
            # make a new node 
            copyNode = Node(node.val, [])
            # store the mapping of current node to new node
            hashMap[node] = copyNode
            # for node in neighbors of current node
            for destination in node.neighbors:
                # if the node is not in the visited set
                if destination not in visitedSet:
                    # do a dfs
                    dfs(destination, visitedSet, hashMap)
                # add the node to the new nodes neighbors
                copyNode.neighbors.append(hashMap[destination])
        
        dfs(node, visitedSet, hashMap)
        return hashMap[node]

def main():
    root = Node(5)
    root.neighbors.append(Node(6))
    root.neighbors.append(Node(7))
    root.neighbors.append(Node(8))
    mySol = Solution()
    print(root == mySol.cloneGraph(root))

if __name__ == "__main__":
    main()