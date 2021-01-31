class Solution:
    def numDecodings(self, s):
        sz = len(s)
        dp = [0 for i in range(sz + 1)]
        # 1 way to decode 0 letters, empty string
        dp[0] = 1
        # if first digit is 0, there are no ways of decoding it
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        # for the rest of the string add number of ways for 2 cases:
        # only 1 digit is taken into consideration, 2 digits are taken into consideration
        for i in range(2, sz + 1):
            oneDigit = int(s[i - 1])
            twoDigit = int(s[i - 2: i])
        
            if oneDigit >=1:
                dp[i] += dp[i - 1]
            
            if twoDigit >= 10 and twoDigit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[sz]

def main():
    mySol = Solution()
    print("The number of ways to decode 226 is " + str(mySol.numDecodings("226")))

if __name__ == "__main__":
    main()