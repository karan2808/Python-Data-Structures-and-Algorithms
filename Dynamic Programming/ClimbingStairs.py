class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        # only 1 way to climb 1 step
        dp[1] = 1
        # two ways to climb 2 step, 1 step twice or 2 steps at once
        dp[2] = 2
        # for step 3 onwards, num ways = num ways for previous step + num ways for 2 steps back
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def main():
    mySol = Solution()
    print("The number of unique ways to climb 3 steps are " +
          str(mySol.climbStairs(3)))
    print("The number of unique ways to climb 6 steps are " +
          str(mySol.climbStairs(6)))


if __name__ == "__main__":
    main()
