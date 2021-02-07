class Solution:
    def findPivot(self, nums):
        # find the total sum of nums
        total = 0
        for num in nums:
            total += num

        # keep a track of left sum
        leftsum = 0
        for i in range(len(nums)):
            # if total - sum of all elements to left of current element - current element value == leftsum, we have a pivot index
            if leftsum == total - leftsum - nums[i]:
                return i
            
            leftsum += nums[i]
        
        return -1

def main():
    mySol = Solution()
    nums = [1, 2, -1, 5, 8, -6, 1, 12, 4, -3, -2, 1]
    print("For the array " + str(nums) + " the pivot index is " + str(mySol.findPivot(nums)))

if __name__ == "__main__":
    main()