# Subsets: Given an int array nums of unique elements, the goal is to return all possible subsets of the power set.

class Solution:
    def solve(self, result, nums, combination, idx, n):
        if n == 0:
            return
        if idx <= n:
            result.append(combination[:])
        for i in range(idx, n):
            self.solve(result, nums, combination + [nums[i]], i + 1, n)

    def subsets(self, nums):
        result = []
        self.solve(result, nums, [], 0, len(nums))
        return result

def main():
    mySol = Solution()
    print("The subsets of 1, 2, 3 ")
    print(mySol.subsets([1, 2, 3]))

if __name__ == "__main__":
    main()
