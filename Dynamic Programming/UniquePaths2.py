from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        if rows == 0:
            return 0
        cols = len(obstacleGrid[0])

        # make a dp array
        dp = [[0 for i in range(cols)] for i in range(rows)]

        # for going all the way right and all the way down from starting position, there's only one way
        # if an obstacle is encountered, we cannot go further
        for i in range(rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(cols):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        # two ways of arriving at each cell, from top or left, if an obstacle is present, num ways are 0
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[rows-1][cols-1]


def main():
    mySol = Solution()
    gird = [[0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]]
    print("The number of ways of arriving to the end position given the grid ")
    print(gird)
    print("is, " + str(mySol.uniquePathsWithObstacles(gird)))


if __name__ == "__main__":
    main()
