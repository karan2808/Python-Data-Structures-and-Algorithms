class Solution:
    def longestValidParentheses(self, s):
        maxIdx = 0
        # maintain a stack to store the indices
        stackIdx = []
        stackIdx.append(-1)
        for i in range(len(s)):
            # if an opening bracket is encountered, push the index to stack
            if s[i] == '(':
                stackIdx.append(i)
            else:
                # for closing braces pop the idx
                stackIdx.pop()
                # if stack is empty, append index to start a new parentheses string
                if len(stackIdx) == 0:
                    stackIdx.append(i)
                else:
                    # get the max idx, subtract stack top from current index
                    maxIdx = max(maxIdx, i - stackIdx[-1])
        return maxIdx

def main():
    mySol = Solution()
    print("The length of longest valid parentheses ")
    print(mySol.longestValidParentheses("()()(()))(()())))"))

if __name__ == "__main__":
    main()