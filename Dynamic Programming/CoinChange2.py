class Solution:
    def change(self, amount, coins):
        dp = [0 for i in range(amount + 1)]
        # for amount 0, you can have 1 combination, do not include any coin
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                # add i - coin dp value, the number of combinations excluding current coin, to current dp value
                dp[i] += dp[i - coin]
        return dp[amount]


def main():
    mySol = Solution()
    print("For the coins 1, 2, 3, 5, and amount 11, the number of combinations to make up the amount are ")
    print(mySol.change(11, [1, 2, 3, 5]))
    print("For the coins 1, 2, 5, and amount 5, the number of combinations to make up the amount are ")
    print(mySol.change(5, [1, 2, 5]))


if __name__ == "__main__":
    main()
