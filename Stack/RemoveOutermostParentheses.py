class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        ans = ""
        # For every character in S
        for c in S:
            # if an opening bracket is encountered
            if c == "(":
                # if there is an element in the stack, we are at the second opening bracket
                if len(stack) >= 1:
                    ans += "("
                    stack.append(c)
                else:
                    stack.append(c)
            else:
                # if there is an element on the stack, its the outermost opening bracket
                if len(stack) > 1:
                    ans += ")"
                    stack.pop()
                else:
                    stack.pop()
        return ans


def main():
    mySol = Solution()
    S = "((()))(()()())"
    print("After removing the outer parentheses of " +
          S + " we get " + mySol.removeOuterParentheses(S))


if __name__ == "__main__":
    main()
