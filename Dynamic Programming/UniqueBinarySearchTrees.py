class Solution:
    # for bsts with 4 nodes, 
    # fix 1st node and make bsts with 3 nodes, 
    # fix 2nd node and make bsts with 2 nodes on right, on left, make bsts with one node
    # similarly for 3rd node we make bsts with 2 nodes on left and one on right
    # for 4th node we make bsts with 3 nodes on left
    # i = 0, 1, 2, 3->
    # bsts += dp[0] * dp[3] + dp[1] * dp[2] + dp[2] * dp[1] + dp[3] * dp[0]
    def getCount(self, dp, current):
        total = 0
        for i in range(0, current):
            total += dp[i] * dp[current - i - 1]
        return total

    def numTrees(self, n):
        # if n = 1, only 1 tree possible, if 2, only 2 trees possible
        if n == 1:
            return 1
        if n == 2:
            return 2

        # make a dp array
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        # for the rest of n, 
        for i in range(3, n + 1):
            dp[i] = self.getCount(dp, i)
        
        return dp[n]