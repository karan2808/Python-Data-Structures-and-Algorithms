class Solution:
    def nextGreaterElement(self, nums1, nums2):
        hashMap = {}
        stack = []

        # for each number in nums2
        for i in range(len(nums2)):
            # if the stack is empty, push element onto it
            if len(stack) == 0:
                stack.append(nums2[i])
            else:
                # find next greater element for each num and store it in hash map
                while len(stack) > 0 and nums2[i] > stack[-1]:
                    hashMap[stack[-1]] = nums2[i]
                    stack.pop()
                # push current node onto stack
                stack.append(nums2[i])

        # for numbers that dont have greater numbers
        while len(stack):
            hashMap[stack[-1]] = -1
            stack.pop()

        # store the next greater nums in nums1
        for i in range(len(nums1)):
            nums1[i] = hashMap[nums1[i]]

        return nums1


def main():
    mySol = Solution()
    nums1 = [4, 1, 2, 3]
    nums2 = [1, 3, 4, 2]
    print(
        "For nums1 [4, 1, 2, 3] and nums2 [1, 3, 4, 2], the next greater elements: ")
    print(mySol.nextGreaterElement(nums1, nums2))


if __name__ == "__main__":
    main()
