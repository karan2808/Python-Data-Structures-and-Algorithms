class Solution:
    def nextLargerNodes(self, head):
        if not head:
            return []

        result = []
        stack = []

        currIdx = 0
        while head:
            # while there are elements on stack and stack top value is less than current value
            while len(stack) > 0 and stack[-1][1] < head.val:
                # result at the index of stack top value will be current value
                result[stack[-1][0]] = head.val
                stack.pop()

            # push current value on to stack and increment index
            stack.append([currIdx, head.val])
            currIdx = currIdx + 1

            # append 0 to result
            result.append(0)
            head = head.next

        return result

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main():
    mySol = Solution()
    node = ListNode(2)
    node.next = ListNode(1)
    node.next.next = ListNode(5)
    node.next.next.next = ListNode(7)
    print("The next larger nodes for nodes 2, 1, 5, 7 are " +
          str(mySol.nextLargerNodes(node)))


if __name__ == "__main__":
    main()
