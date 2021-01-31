class Solution:
    def findMax(self, prices, current, numDays, dp):
        if (current >= numDays):
            return 0

        # if dp value is present, return it
        if (dp[current] != -1):
            return dp[current]

        maxVal = 0

        for i in range(current + 1, numDays):
            if prices[current] < prices[i]:
                # buy on current day and sell on day i, prices[i] is the amount earned, prices[current] is amount lost,
                # cannot buy on the next day, check max profit from day i + 2 onwards
                maxVal = max(
                    maxVal, prices[i] - prices[current] + self.findMax(prices, i + 2, numDays, dp))

        # move on to the next day
        maxVal = max(maxVal, self.findMax(prices, current + 1, numDays, dp))

        dp[current] = maxVal
        return maxVal

    def maxProfit(self, prices):
        sz = len(prices)
        if sz <= 1:
            return 0
        dp = [-1 for i in range(sz + 1)]
        return self.findMax(prices, 0, sz, dp)


def main():
    prices = [1, 2, 3, 0, 2]
    mySol = Solution()
    print("The max profit from prices 1, 2, 3, 0, 2 ")
    print(mySol.maxProfit(prices))


if __name__ == "__main__":
    main()
