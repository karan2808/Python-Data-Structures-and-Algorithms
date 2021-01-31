# Longest Palindromic Substring: Given a string s, the goal is to find the longest palindromic substring in s.

class Solution:
    def expandCenter(self, i, j, s):
        lenS = len(s)
        # expand around center until the string becomes non palindromic
        while (i >= 0 and j < lenS and s[i] == s[j]):
            i = i - 1
            j = j + 1
        # return the substring
        return s[i+1: j]

    def longestPalindrome(self, s):
        lenS = len(s)
        res = ""
        for i in range(lenS):
            # expand and check for palindromic sequence of odd length
            tempPalin = self.expandCenter(i, i, s)
            if len(tempPalin) > len(res):
                res = tempPalin
            # expand and check for palindromic sequence of even length
            if i + 1 < lenS:
                tempPalin = self.expandCenter(i, i + 1, s)
                if len(tempPalin) > len(res):
                    res = tempPalin
        return res

def main():
    mySol = Solution()
    print("Longest Palindromic substring for the string aabaabccabgjkslmlskjroggorjkslstrewerts is ")
    print(mySol.longestPalindrome("aabaabccabgjkslmlskjroggorjkslstrewerts"))

if __name__ == "__main__":
    main()