class Solution:
    def removeDuplicates(self, S):
        stack = []
        stack.append(S[0])

        for i in range(1, len(S)):
            # if we encounter the same char again,
            if len(stack) and stack[-1] == S[i]:
                stack.pop()
                continue
            # push the element and check for adj elements in the next iter
            stack.append(S[i])

        st = ""
        while len(stack):
            st += stack.pop()
        
        st = st[::-1]
        return st

def main():
    mySol = Solution()
    print("After removing duplicates from abbaca, the new string is " + str(mySol.removeDuplicates("abbaca")))

if __name__ == "__main__":
    main()