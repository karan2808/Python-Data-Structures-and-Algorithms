class Solution:
    def fourSum(self, nums, target):

        # function to find k sum
        def kSum(nums, target, k):
            # if we exhaust all the numbers in nums, or if we exceede target, or if the target cannot be reached
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []

            if k == 2:
                # compute 2 sum and return
                return twoSum(nums, target)
            
            res = []
            for i in range(len(nums)):
                # since we need unique sets
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)

            return res
        
        def twoSum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                # check if the number is not already in result
                if len(res) == 0 or res[-1][1] != nums[i]:
                    # if the difference is in the set
                    if target - nums[i] in s:
                        # append the difference and nums to result
                        res.append([target - nums[i], nums[i]])
                    # add nums to set
                    s.add(nums[i])
            return res
        nums.sort()
        return kSum(nums, target, 4)

def main():
    mySol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    print("Combinations generated given nums: [1, 0, -1, 0, -2, 2] and sum = 0 are " + str(mySol.fourSum(nums, 0)))

if __name__ == "__main__":
    main()