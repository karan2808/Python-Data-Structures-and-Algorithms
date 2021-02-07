class Solution:
    def firstMissingPositive(self, nums, numNumber):
        # check if the array has a 1
        has1 = False
        for i in range(numNumber):
            if nums[i] == 1:
                has1 = True
            # if the number is negative or out of bonds, set it to 1
            if (nums[i] <= 0 or nums[i] > numNumber):
                nums[i] = 1
        
        # if the array does not have 1 return 1
        if not has1:
            return 1

        # go over the array and set the positive numbers to negative
        for i in range(numNumber):
            # convert num to an index
            idx = abs(nums[i] - 1)
            # if num is greater than 0, set it to a negative value
            if nums[i] > 0:
                nums[i] = -nums[i]

        # get the first positive, its index will be the missing number
        for i in range(numNumber):
            if nums[i] > 0:
                return i + 1
        
        return numNumber + 1

def main():
    mySol = Solution()
    nums = [-1, -2, 1, 3, 4, 90]
    print("The first missing positive for nums [-1, -2, 1, 3, 4, 90] is " + str(mySol.firstMissingPositive(nums, 6)))

if __name__ == "__main__":
    main()