class Solution:
    def isMatch(self, s, p):
        # make a dp matrix
        dp = [[False for i in range(len(s) + 1)] for i in range(len(p) + 1)]
        # 0 letters will match
        dp[0][0] = True
        # if previous letter is '*' whether the strings match depends on the dp value before that letter
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i-2]

        # fill the dp matrix
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # if the prev letter is '.' or if letters are the same
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # check rest of the pattern before that letter
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # check two characters back
                    dp[i][j] = dp[i][j-2]
                    # if we have a . two characters back
                    # if char at two steps back in the pattern is same as prev char in s
                    if p[j - 2] == '.' or p[j - 2] == s[i-1]:
                        dp[i][j] = dp[i][j] | dp[i-1][j]
                else:
                    # we dont have a match
                    dp[i][j] = False
        return dp[len(s)][len(p)]


def main():
    mySol = Solution()
    s = "ab"
    p = ".*"
    if mySol.isMatch(s, p):
        isM = "is a match"
    else:
        isM = "is not a match"
    print("The string ab and pattern .* " + isM)
    s = "ab"
    p = "ac"
    if mySol.isMatch(s, p):
        isM = "is a match"
    else:
        isM = "is not a match"
    print("The string ab and pattern ac " + isM)


if __name__ == "__main__":
    main()
