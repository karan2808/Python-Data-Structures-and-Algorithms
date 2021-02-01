class Solution:
    def decodeString(self, s):

        sz = len(s)
        res = ""
        result = []
        counts = []

        index = 0

        while index < sz:
            # if the current char is a digit
            if s[index].isdigit():
                count = 0
                # while we have digits, convert them to int
                while s[index].isdigit():
                    count = count * 10 + int(s[index])
                    index += 1
                # push count onto stack
                counts.append(count)
            
            # when an opening bracket is encountered, push the current result on to stack and increment index
            # also reset the result
            elif s[index] == '[':
                result.append(res)
                res = ""
                index += 1
            
            # if a closing bracket is encountered, get the top result value, get the count value
            # append current result to top result value on stack count number of times
            elif s[index] == ']':
                temp = result[-1]
                count = counts[-1]
                result.pop()
                counts.pop()

                # for count, append the top most string from stack to temp
                while count:
                    temp += res
                    count -= 1
                res = temp
                index += 1
            
            # add the char to current result, given char is not a digit or bracket
            else:
                res += s[index]
                index += 1
        
        return res

def main():
    mySol = Solution()
    print("The decoded version of 3[a2[bc]4[de]] is ")
    print(mySol.decodeString("3[a2[bc]4[de]]"))

if __name__ == "__main__":
    main()