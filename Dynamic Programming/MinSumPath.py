from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        # can go down only, for the first column
        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        
        # can go right only, for the first row
        for i in range(1, cols):
            grid[0][i] += grid[0][i-1]
        
        # for every cell we have 2 options, to arrive from top or from left, we take min of the two
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        
        return grid[rows-1][cols-1]


def main():
    mySol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print("The min sum path for the grid ")
    print(grid)
    print("is: " + str(mySol.minPathSum(grid)))
    grid = [[1,2,3],[4,5,6]]
    print("The min sum path for the grid ")
    print(grid)
    print("is: " + str(mySol.minPathSum(grid)))

if __name__ == "__main__":
    main()