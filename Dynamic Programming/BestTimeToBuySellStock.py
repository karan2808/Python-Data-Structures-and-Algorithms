# Best Time to Buy and Sell Stock: Given an array of prices where prices[i] is the price of a given stock on the ith day.

class Solution:
    def maxProfit(self, prices):
        maxProf = 0
        minVal = float('inf')
        for i in range(len(prices)):
            # keep updating the minVal
            if minVal > prices[i]:
                minVal = prices[i]
            # maxprofit is the difference between prices[i] and min value
            maxProf = max(maxProf, prices[i] - minVal)
        return maxProf


def main():
    mySol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print("Max profit given the prices 7, 1, 5, 3, 6, 4 is ")
    print(mySol.maxProfit(prices))


if __name__ == "__main__":
    main()
