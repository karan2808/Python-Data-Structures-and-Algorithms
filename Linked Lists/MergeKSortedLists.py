class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def merge2Lists(self, l1, l2):
        head = ListNode(0)
        temp = head

        while l1 and l2:
            # if l2 val is greater, heads next is l1
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                # if l1 is greater, heads next is l2
                head.next = l2
                l2 = l2.next

            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return temp.next

    def mergeKLists(self, lists):
        interval = 1
        lenList = len(lists)
        # if the length is 0, return null
        if (lenList == 0):
            return None

        while interval < lenList:
            # first merge two at a time, then 4 at a time and so on
            for i in range(0, lenList - interval, 2 * interval):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]


def printList(root):
    s = ""
    while root:
        s += str(root.val) + " "
        root = root.next
    print(s)


def main():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    listOfroots = [l1, l2, l3]
    mySol = Solution()
    finalRoot = mySol.mergeKLists(listOfroots)
    printList(finalRoot)


if __name__ == "__main__":
    main()
