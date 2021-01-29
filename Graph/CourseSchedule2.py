class Solution:
    def __init__(self):
        self.stack = []
    
    def dfs(self, adj, visited, v):
        visited[v] = 1
        for i in range(len(adj[v])):
            if visited[adj[v][i]] == 0:
                self.dfs(adj, visited, adj[v][i])
        self.stack.append(v)

    def isCycleUtil(self, adj, v, visited):
        # if node in gray set, return true
        if visited[v] == 1:
            return True
        if visited[v] == 2:
            return False
        visited[v] = 1
        for i in range(len(adj[v])):
            if self.isCycleUtil(adj, adj[v][i], visited):
                return True
        visited[v] = 2
        return False

    # 3 set approach
    def isCycle(self, adj, numCourses):
        visited = [0 for i in range(numCourses)]
        # go through each node, if not visited, check for cycles
        for i in range(numCourses):
            # if the node is not visited
            if not visited[i]:
                if self.isCycleUtil(adj, i, visited):
                    return True
        return False

    def findOrder(self, numCourses, prerequisites):
        courses = []
        # adjacency list
        adj = [[] for i in range(numCourses)]
        prereq_sz = len(prerequisites)
        # make the adjacency list
        for i in range(prereq_sz):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        # check for cycles, if there is a cycle, you cannot complete all courses
        if self.isCycle(adj, numCourses):
            print("Cant complete all courses")
            return courses 
        
        # do a dfs and add courses to the stack
        visited = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                self.dfs(adj, visited, i)
        self.stack.reverse()
        return self.stack

def main():
    mySol = Solution()
    prerequisites1 = [[1, 0], [0, 1], [2, 0]]
    prerequisites2 = [[1, 0], [2, 0], [3, 0], [4, 3], [5, 4]]
    print("To finish all courses with prerequisites: [[1, 0], [0, 1], [2, 0]], the order which should be followed is")
    print(str(mySol.findOrder(3, prerequisites1)))
    print("To finish all courses with prerequisites: [[1, 0], [2, 0], [3, 0]], the order which should be followed is")
    print(str(mySol.findOrder(6, prerequisites2)))

if __name__ == "__main__":
    main()
