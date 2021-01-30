# Permutations: Given an array nums of distinct integers, return all possible permutations.

class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        
        # back track
        def backTrack(nums, path):
            # if nums are exhausted,append path and return
            if not nums:
                result.append(path)
            # go though each num
            for i in range(0, len(nums)):
                backTrack(nums[:i] + nums[i+1:], path + [nums[i]])

        # back track return the result    
        result = []
        backTrack(nums, path = [])
        return result

def main():
    mySol = Solution()
    print("Permutations for the nums 1, 2, 3 are ")
    print(mySol.permute([1, 2, 3]))

if __name__ == "__main__":
    main()