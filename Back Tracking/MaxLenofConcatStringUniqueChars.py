# Maximum Length of a Concatenated String with Unique Characters: Given an array of strings arr, string s is a concatenation of sub-sequence of arr such that s has unique characters. The objective is to return the maximum possible length of s. 

class Solution:
    def __init__(self):
        self.result = []
        self.maxSz = 0

    def backTrack(self, arr, combination, idx):
        if self.isUnique(combination):
            self.maxSz = max(self.maxSz, len(combination))
        if idx > len(arr):
            return
        # add current array element to combination and back track
        for i in range(idx, len(arr)):
            self.backTrack(arr, combination + arr[i], i + 1)

    # function to check if a string is unique
    def isUnique(self, combination):
        # for every char, check if its present in the dictionary
        # if its already present, string does not have unique chars
        charDict = {}
        for c in combination:
            if c in charDict.keys():
                return False
            charDict[c] = 1
        return True

    def maxLength(self, arr):
        combination = ""
        self.backTrack(arr, combination, 0)
        return self.maxSz

def main():
    mySol = Solution()
    arr = ["un", "iq", "ue"]
    print("Maximum size of a unique string formed using a sub array of ")
    print(arr)
    print("=")
    print(mySol.maxLength(arr))

if __name__ == "__main__":
    main()