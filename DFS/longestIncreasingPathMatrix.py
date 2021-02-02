class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.cache = None
    
    def dfs(self, matrix, row, col, rows, cols):
        # if the value is present in cache, return it
        if self.cache[row][col] > 0:
            return self.cache[row][col]
        
        maxVal = 0
        # for every direction up down left right
        for dir_ in self.directions:
            x = row + dir_[0]
            y = col + dir_[1]
            # if we are in the bounds of the matrix and the path is increasing, update max val
            if x >= 0 and y >= 0 and x < rows and y < cols and matrix[x][y] > matrix[row][col]:
                maxVal = max(maxVal, self.dfs(matrix, x, y, rows, cols))
        
        # increase max path by 1 and store it in cache
        self.cache[row][col] = maxVal + 1
        return self.cache[row][col]

    def longestIncreasingPath(self, matrix):

        # get the size of the matrix and resize the cache
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])

        self.cache = [[0 for i in range(cols + 1)] for i in range(rows + 1)]
        maxPath = 0

        # go a dfs and keep updating maxPath
        for i in range(rows):
            for j in range(cols):
                maxPath = max(maxPath, self.dfs(matrix, i, j, rows, cols))

        return maxPath

def main():
    Matrix = [[9,9,4],[6,6,8],[2,1,1]]
    mySol = Solution()
    print("The max increasing path for Matrix ")
    print(Matrix)
    print("is " + str(mySol.longestIncreasingPath(Matrix)))

if __name__ == "__main__":
    main()