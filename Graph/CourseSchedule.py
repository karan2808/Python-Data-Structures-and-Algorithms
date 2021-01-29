class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        sz = len(prerequisites)
        # make the adjacency list
        for i in range(sz):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        # if there is a cycle, return false
        if self.isCycle(adj, numCourses):
            return False
        return True

    # make 3 sets, white, gray, black
    # keep all nodes in white set, 
    # put a node in gray set and start exploring its neighbors
    # put the explored node in black set
    # if while exploring a node is found in gray set, there is a cycle
    def is_cycle_util(self, adj, visited, v):
        if visited[v] == 1:
            return True
        if visited[v] == 2:
            return False
        visited[v] = 1
        # explore the neighbors of current node
        for i in range(len(adj[v])):
            # check if cycle for neighbors
            if (self.is_cycle_util(adj, visited, adj[v][i])):
                return True
        return False
    
    def isCycle(self, adj, numCourses):
        visited = [0 for i in range(numCourses)]
        # go through all the courses
        for i in range(numCourses):
            # if not visited, check for cycle
            if not visited[i]:
                # check cycle util
                if self.is_cycle_util(adj, visited, i):
                    return True
        return False

def main():
    mySol = Solution()
    prerequisites1 = [[1, 0], [0, 1], [2, 0]]
    prerequisites2 = [[1, 0], [2, 0], [3, 0]]
    if mySol.canFinish(3, prerequisites1):
        s1 = "Can Finish"
    else:
        s1 = "Cannot Finish"
    if mySol.canFinish(4, prerequisites2):
        s2 = "Can Finish"
    else:
        s2 = "Cannot Finish"
    print("Can you finish all courses with prerequisites: [[1, 0], [0, 1], [2, 0]]? ")
    print(s1)
    print("Can you finish all courses with prerequisites: [[1, 0], [2, 0], [3, 0]]? ")
    print(s2)

if __name__ == "__main__":
    main()