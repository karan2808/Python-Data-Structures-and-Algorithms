import random

class Solution:
    def pickTfromN(self, nums, k):
        # get the size of nums
        sz = len(nums)

        result = []

        for i in range(k): # O(k)
            # pick a random number 
            randIdx = random.randrange(0, sz - 1)

            # store the number at random idx in result
            result.append(nums[randIdx])

            # remove the random number from nums O(N)
            nums.pop(randIdx)
            
            # decrement the size
            sz -= 1

        return result

def main():
    mySol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    print(mySol.pickTfromN(nums, 3))

if __name__ == "__main__":
    main()