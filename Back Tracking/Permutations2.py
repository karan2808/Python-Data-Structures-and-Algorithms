# Permutations2: Given an array nums of integers that can contain duplicates, return all possible unique permutations.

from collections import Counter

class Solution:
    def permuteUnique(self, nums):
        result = []
        def backtrack(combination, counter):
            if len(combination) == len(nums):
                result.append(combination[:])
            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    combination.append(num)
                    # decrement count so its not used again
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(combination, counter)
                    # revert the choice for next exploration
                    combination.pop()
                    # increment the count again
                    counter[num] += 1
        # make a hash map of counts, and back track
        backtrack([], Counter(nums))
        return result

def main():
    mySol = Solution()
    nums = [1, 2, 3]
    print("The unique permutations of nums 1, 2, 3, are ")
    print(mySol.permuteUnique(nums))

if __name__ == "__main__":
    main()