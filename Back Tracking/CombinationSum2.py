# Combination Sum 2: Given an array of distinct integer candidates and a target integer value, the objective is to find all unique combinations of candidates where the chosen numbers sum to target. Each number in candidates may only be used once.

class Solution:
    def combinationSum2(self, candidates, target):
        # sort the candidates to make it easier to calculate sum
        candidates.sort()
        result = []
        # dfs + back tracking
        self.dfs(result, [], 0, candidates, target)
        return result

    def dfs(self, result, combination, index, candidates, target):
        # if target goes to 0, a combination is found, append a copy of combinaiton to resut
        if target == 0:
            result.append(combination[:])
            return

        for i in range(index, len(candidates)):
            # check necessary conditions, so that no duplicates are generated
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(result, combination +
                     [candidates[i]], i, candidates, target - candidates[i])


def main():
    mySol = Solution()
    candidates = [2, 3, 6, 7, 4, 2, 5, 9, 1]
    print("Possible combinations (excluding duplicates) that sum to 7 are ")
    print(mySol.combinationSum2(candidates, 7))


if __name__ == "__main__":
    main()
