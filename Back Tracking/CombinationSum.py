# Combination Sum: Given an array of distinct integer candidates and a target integer value, the objective is to find all unique combinations of candidates where the chosen numbers sum to target.

class Solution:
    def combinationSum(self, candidates, target):
        def findCombinations(combinations, candidates, target, idx):
            # if target reaches 0, we find a valid combination
            if target == 0:
                result.append(combinations)
                return
            # check if more numbers can be added to give the target sum
            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    break
                findCombinations(
                    combinations + [candidates[i]], candidates, target - candidates[i], i)

        result = []
        # if no candidates, return result
        if len(candidates) == 0:
            return result
        # sort the candidates
        candidates.sort()
        # find combinations using back tracking
        findCombinations([], candidates, target, 0)
        return result

def main():
    mySol = Solution()
    candidates = [2, 3, 6, 7, 4, 2, 5, 9, 1]
    print("All possible combinations that sum to 7 are ")
    print(mySol.combinationSum(candidates, 7))

if __name__ == "__main__":
    main()
