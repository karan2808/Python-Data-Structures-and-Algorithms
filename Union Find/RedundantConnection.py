class DSU:
    def __init__(self, sz):
        self.parent = []
        self.rank = []
        # each node is its own parent, and rank is initially 0
        for i in range(sz + 1):
            self.parent.append(i)
            self.rank.append(0)

    def find(self, x):
        # find parent until the parent of the node is not itself
        if self.parent[x] != x:
            # collapse nodes to a single parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        # if the nodes have a common parent, return true
        if parent_x == parent_y:
            return True
        
        # else check the ranks
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        
        elif self.rank[parent_y] < self.rank[parent_x]:
            self.parent[parent_y] = parent_x
        
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1
        # no common parent
        return False
    
class Solution:
    def findRedundantConnection(self, edges):
        sz = len(edges)
        dsu = DSU(sz)

        for i in range(sz):
            if dsu.union(edges[i][0], edges[i][1]):
                return edges[i]
        return []

def main():
    mySol = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    print("The redundant edge in " + str(edges) + " is " + str(mySol.findRedundantConnection(edges)))

if __name__ == "__main__":
    main()