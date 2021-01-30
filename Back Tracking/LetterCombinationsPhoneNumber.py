# Letter Combinations of a Phone Number: Given a string containing digits from 2-9 inclusive, the objective is to return all possible letter combinations that the number could represent.

class Solution:
    def coder(self, ch):
        if (ch == 2):
            return "abc"
        if (ch == 3):
            return "def"
        if (ch == 4):
            return "ghi"
        if (ch == 5):
            return "jkl"
        if (ch == 6):
            return "mno"
        if (ch == 7):
            return "pqrs"
        if (ch == 8):
            return "tuv"
        if (ch == 9):
            return "wxyz"
        else:
            return ""
    
    # for every position we have 3 options so time complexity = 3^(len of digits).
    # Space complexity will be the same, since recursion allocates space on stack
    def find(self, digits, combination, result):
        # if all digits are used, append combination to result and return
        if len(digits) == 0:
            result.append(combination[:])
            return
        # get the first character
        ch = digits[0]
        # get the code for the character
        code = self.coder(int(ch))
        for i in range(len(code)):
            # for each letter in the code, find a combination
            self.find(digits[1:], combination + code[i], result)

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        result = []
        self.find(digits, "", result)
        return result

def main():
    mySol = Solution()
    ip = "23"
    print("The combinations for input 23 are ")
    print(mySol.letterCombinations(ip))


if __name__ == "__main__":
    main()