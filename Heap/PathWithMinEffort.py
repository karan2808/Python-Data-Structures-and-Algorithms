from heapq import heapify, heappop, heappush
class Solution:
    def minimumEffortPath(self, heights):
        # get the max rows and cols
        m, n = len(heights), len(heights[0])
        # make a heap to store the current min cost, x, and y
        heap = [(0, 0, 0)]
        # keep track of current cost
        currCost = 0
        # keep track of the nodes you have visited
        visited = set()
        # make a directions array
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while heap:
            # get the min cost val, x and y coordinate
            k, x, y = heappop(heap)
            # update the cost
            currCost = max(currCost, k)
            # if we reach the bottom right corner, return the cost
            if (x, y) == (m -1, n - 1):
                return currCost

            # add current node to the visited set
            visited.add((x, y))

            # for each direction, find the new cost
            for dir_ in directions:
                xn = x + dir_[0]
                yn = y + dir_[1]

                # check boundary conditions and if the cell has been visited
                if 0 <= xn <= m - 1 and 0 <= yn <= n - 1 and (xn, yn) not in visited:
                    # get new cost
                    newc = abs(heights[x][y] - heights[xn][yn])
                    # push the new x, y location and the new cost to min heap
                    heappush(heap, (newc, xn, yn))

        # if no path, return -1
        return -1

def main():
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    mySol = Solution()
    print("The min cost path for the grid heights = [[1,2,2],[3,8,2],[5,3,5]] is " + str(mySol.minimumEffortPath(heights)))

if __name__ == "__main__":
    main()