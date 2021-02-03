class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors != None else []


class Solution:
    def __init__(self):
        self.clonesBfs = {}

    def cloneGraph(self, root):
        if root == None:
            return None
        
        # make a new head
        currentClone = Node(val = root.val)

        # update the hash map
        self.clonesBfs[root] = currentClone

        # make a queue for bfs
        nodesQ = []
        nodesQ.append(root)

        while len(nodesQ) != 0:
            # get the size of the queue and do a bfs
            sz = len(nodesQ)

            for k in range(sz):
                currentNode = nodesQ.pop(0)

                # make a clone for all neighbos
                for currentNeighbor in currentNode.neighbors:
                    # if current neighbor not found in clones list
                    if currentNeighbor not in self.clonesBfs.keys():
                        self.clonesBfs[currentNeighbor] = Node(currentNeighbor.val)
                        # push the neighbor onto queue
                        nodesQ.append(currentNeighbor)

                    # append the neighbor clone to current node
                    self.clonesBfs[currentNode].neighbors.append(self.clonesBfs[currentNeighbor])

        return currentClone


def main():
    root = Node(5)
    root.neighbors.append(Node(6))
    root.neighbors.append(Node(7))
    root.neighbors.append(Node(8))
    root.neighbors.append(Node(9))
    root.neighbors[0].neighbors.append(Node(10))
    mySol = Solution()
    print(root == mySol.cloneGraph(root))

if __name__ == "__main__":
    main()
    