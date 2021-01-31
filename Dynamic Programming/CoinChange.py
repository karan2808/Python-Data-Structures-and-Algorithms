class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            # for each coin, 
            for coin in coins:
                # if the denomination is less than current amount
                if coin <= i:
                    # dp[i] = minimum of current dp[i] and by fixing current coin and taking dp of current amount - coin
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]


def main():
    mySol = Solution()
    print("For the coins 1, 2, 3, 5, and amount 11, the fewest number of coins to make up the amount are ")
    print(mySol.coinChange([1, 2, 3, 5], 11))


if __name__ == "__main__":
    main()
