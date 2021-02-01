class Solution:
    def buildArray(self, target, n):
        ops = []
        i, j = 1, 0
        stack = []
        while i <= n and j < len(target):
            stack.append(i)
            ops.append("Push")
            if stack[-1] == target[j]:
                i += 1
                j += 1
            else:
                ops.append("Pop")
                i += 1

        return ops

def main():
    mySol = Solution()
    print("Operations for array 1, 3 and n = 3: ")
    print(mySol.buildArray([1, 3], 3))

if __name__ == "__main__":
    main()