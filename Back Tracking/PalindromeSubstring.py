# Palindrome Partitioning: Given a string s, partition s, such that every substring of the parition is a palindrome. The goal is to find all possible partitioning of s.

class Solution:
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True
    
    def dfs(self, s, start, currentList, result):
        # if all characters are used, append to result
        if start >= len(s):
            result.append(currentList[:])
        for end in range(start, len(s)):
            # check if string is a palindrome 
            if self.isPalindrome(s, start, end):
                # get the substring and add to current list
                self.dfs(s, end + 1, currentList + [s[start:end+1]], result)
    
    def partition(self, s):
        result = []
        self.dfs(s, 0, [], result)
        return result

def main():
    mySol = Solution()
    print("All possible palindrome partitions of aababc are")
    print(mySol.partition("aababc"))

if __name__ == "__main__":
    main()