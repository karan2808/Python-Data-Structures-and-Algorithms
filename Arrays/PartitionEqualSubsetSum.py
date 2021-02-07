class Solution:
    def canPartition(self, nums):
        sz = len(nums)
        if sz == 1:
            return False
        
        # find the total sum
        sum_ = 0
        for i in range(sz):
            sum_ += nums[i]

        # if the sum is not divisible by 2 return false
        if (sum_ % 2) != 0:
            return False

        # make a memoization array, 
        memo = [[-1 for i in range(sum_ // 2 + 1)] for i in range(sz + 1)]

        def subSetSum(pos, currentSum):
            # we found half partition
            if currentSum == 0:
                return True
            # if we exceed number of elements or if current sum goes negative, we cant partition
            elif pos >= sz or currentSum < 0:
                return False
            
            # if value in memo, return
            if memo[pos][currentSum] > -1:
                return memo[pos][currentSum]

            # either include current number or dont
            memo[pos][currentSum] = subSetSum(pos + 1, currentSum - nums[pos]) or subSetSum(pos + 1, currentSum)
            return memo[pos][currentSum]

        return subSetSum(0, sum_//2)

def main():
    sol = Solution()
    nums = [1, 5, 11, 5]
    print("Can partition 1, 5, 11, 5? " + str(sol.canPartition(nums)))

if __name__ == "__main__":
    main()