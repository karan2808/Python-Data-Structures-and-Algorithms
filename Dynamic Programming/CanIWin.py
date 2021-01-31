class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal == 0:
            return True
        self.max = maxChoosableInteger
        self.dp = {}

        # if the desired total is greater than sum of numbers, nobody can win
        if desiredTotal > (maxChoosableInteger * (maxChoosableInteger + 1) // 2):
            return False
        
        # use a mask to indicate set bits
        return self.recurse(2** maxChoosableInteger - 1, desiredTotal)
    
    def recurse(self, mask, total):
        # if the current number exceeds total 
        if mask >= 2**(total - 1):
            return True
        if mask in self.dp:
            return self.dp[mask]

        for i in range(self.max):
            if mask & (1 << i):
                newmask = mask & ~(1 << i) # unset the ith bit
                # recurse with new mask and new total
                if self.recurse(newmask, total - i - 1) == False:
                    self.dp[mask] = True
                    return True
        self.dp[mask] = False
        return False

def main():
    mySol = Solution()
    maxChoosableInteger = 10
    desiredTotal = 11
    print("Can player1 win if max choosable number is 10 and desired total is 11")
    if not mySol.canIWin(maxChoosableInteger, desiredTotal):
        print("Cannot win")
    else:
        print("Can win")

    maxChoosableInteger = 30
    desiredTotal = 11
    print("Can player1 win if max choosable number is 30 and desired total is 11")
    if not mySol.canIWin(maxChoosableInteger, desiredTotal):
        print("Cannot win")
    else:
        print("Can win")

if __name__ == "__main__":
    main()

