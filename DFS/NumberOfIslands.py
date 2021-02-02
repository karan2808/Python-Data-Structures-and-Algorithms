class Solution:
    def __init__(self):
        self.n_islands = 0

    def dfs(self, grid, row, col, rows, cols):
        if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == '0':
            return 0

        # set the current cell as 0 so its not visited again
        grid[row][col] = '0'

        # we dont care about each individual cells of land
        self.dfs(grid, row + 1, col, rows, cols)
        self.dfs(grid, row, col + 1, rows, cols)
        self.dfs(grid, row, col - 1, rows, cols)
        self.dfs(grid, row - 1, col, rows, cols)

        # one island found
        return 1

    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # keep updating total number of islands
                    self.n_islands += self.dfs(grid, i, j, rows, cols)
        return self.n_islands


def main():
    mySol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
    print("Total number of islands on the grid ")
    print(grid)
    print("is " + str(mySol.numIslands(grid)))


if __name__ == "__main__":
    main()
