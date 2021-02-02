class Solution:
    def __init__(self):
        self.maxArea = 0

    def dfs(self, grid, row, col, rows, cols):
        # check boundary conditions and if on water
        if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
            return 0

        current = 1
        # set the current value as 0 so its not considered again
        grid[row][col] = 0

        current += self.dfs(grid, row + 1, col, rows, cols)
        current += self.dfs(grid, row, col + 1, rows, cols)
        current += self.dfs(grid, row - 1, col, rows, cols)
        current += self.dfs(grid, row, col - 1, rows, cols)

        return current

    def maxAreaOfIsland(self, grid):
        # get the grid size
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        # go through each item in the grid, run a dfs and update max area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.maxArea = max(
                        self.maxArea, self.dfs(grid, i, j, rows, cols))

        return self.maxArea


def main():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    mySol = Solution()
    print("The max area of land for the grid ")
    print(grid)
    print("is " + str(mySol.maxAreaOfIsland(grid)))

if __name__ == "__main__":
    main()
