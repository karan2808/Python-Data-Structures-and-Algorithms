class Solution:
    def maxSubArray(self, nums):

        # if nums is null return
        sz = len(nums)
        if sz == 0:
            return 0
        
        currMax = nums[0]
        globalMax = currMax

        # keep adding nums until sum is increasing, when sum starts descreasing, reset the current max with current num
        for i in range(1, sz):
            currMax = max(currMax + nums[i], nums[i])
            globalMax = max(currMax, globalMax)

        return globalMax

def main():
    mySol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("The max subarray sum for [-2, 1, -3, 4, -1, 2, 1, -5, 4] is " + str(mySol.maxSubArray(nums)))

if __name__ == "__main__":
    main()