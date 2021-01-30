# Combinations: Given two integers n and k, the goal is to return all possible combinations of k numbers out of 1...n.

class Solution:
    def combine(self, n, k):
        result = []
        def backTrack(kLeft, currComb, idx):
            # if leftover k is 0 append current combination to result
            if kLeft == 0:
                result.append(currComb[:])
            else:
                # increment index, add current idx to current comb, and decrement left over k
                for i in range(idx, n + 1):
                    backTrack(kLeft - 1, currComb + [i], i + 1)
        backTrack(k, [], 1)
        return result

def main():
    mySol = Solution()
    print("Given 8 and 3, all combinations of 3 numbers out of 1...8 are ")
    print(mySol.combine(8, 3))

if __name__ == "__main__":
    main()