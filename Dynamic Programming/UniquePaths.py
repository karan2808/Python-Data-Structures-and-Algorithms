class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        # only 1 unique way to go to cells on the right and down
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # for rest of the cells, there are two options, arrive from top or left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


def main():
    mySol = Solution()
    print("Possible paths for m = 3 and n = 2 are ")
    print(mySol.uniquePaths(3, 2))
    print("Possible paths for m = 3 and n = 7 are ")
    print(mySol.uniquePaths(3, 7))


if __name__ == "__main__":
    main()
