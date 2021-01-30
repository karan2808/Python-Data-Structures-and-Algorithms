# Generate Parenthesis: Given n pairs of parentheses, write a function to generate all combinations of well-formed parantheses.

class Solution:
    def generateParenthesis(self, n):
        def backTrack(S, left, right):
            # if the paranthesis has been formed, append to result and return
            if len(S) == 2 * seq_len:
                result.append(S)
                return
            # if the number of left elements is less sequence 
            if left < seq_len:
                backTrack(S + "(", left + 1, right)
            # if the number of right elements is right sequece
            if left > right:
                backTrack(S + ")", left, right + 1)
        seq_len = n
        result = []
        backTrack("", 0, 0)
        return result

def main():
    mySol = Solution()
    print("Generated paranthesis for n = 3 are ")
    print(mySol.generateParenthesis(3))

if __name__ == "__main__":
    main()