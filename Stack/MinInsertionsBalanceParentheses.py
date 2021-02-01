class Solution:
    def minInsertions(self, S):

        minIns = 0
        # stack size to simulate a stack
        stackSize = 0
        i = 0
        while i < len(S):
            # if an opening bracket is encountered, increment stack size
            if S[i] == "(":
                stackSize += 1
                i += 1
            else:
                # for closing bracket, increment index, if the next element is a closing bracket as well
                if (i + 1 < len(S)) and (S[i + 1] == ")"):
                    i += 1
                else:
                    # otherwise an insertion is required
                    minIns += 1

                # are there elements on the stack
                if stackSize == 0:
                    minIns += 1
                else:
                    stackSize -= 1
                i += 1

        # for the closing brackets left in the stack
        minIns += 2 * stackSize

        return minIns


def main():
    mySol = Solution()
    s1 = "(()))"
    s2 = "())"
    s3 = "))())("
    s4 = "(((((("
    s5 = ")))))))"
    print("The number of insertions to balance " +
          s1 + " is " + str(mySol.minInsertions(s1)))
    print("The number of insertions to balance " +
          s2 + " is " + str(mySol.minInsertions(s2)))
    print("The number of insertions to balance " +
          s3 + " is " + str(mySol.minInsertions(s3)))
    print("The number of insertions to balance " +
          s4 + " is " + str(mySol.minInsertions(s4)))
    print("The number of insertions to balance " +
          s5 + " is " + str(mySol.minInsertions(s5)))


if __name__ == "__main__":
    main()
