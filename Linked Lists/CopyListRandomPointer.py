class Node:
    def __init__(self, val_, next_ = None, random_ = None):
        self.val = val_
        self.next = next_
        self.random = random_
    
class Solution:
    def copyRandomList(self, head):
        # check if head is none
        if head == None:
            return None
        # make a dictionary of nodes
        dict_nodes = {}
        # keep a temp node
        temp = head
        # traverse and add nodes to the dictionary 
        while temp:
            dict_nodes[temp] = Node(temp.val)
            temp = temp.next
        # set temp to head again
        temp = head
        while temp:
            if temp.next != None:
                dict_nodes[temp].next = temp.next
            if temp.random != None:
                dict_nodes[temp].random = temp.random
            temp = temp.next
        # return copy of head
        return dict_nodes[head]

def main():
    mySol = Solution()
    root = Node(7)
    root.next = Node(13, None, root)
    root.next.next = Node(11)
    root.next.next.next = Node(10, None, root.next.next)
    root.next.next.next.next = Node(55, None, root.next)
    newRoot = mySol.copyRandomList(root)
    if newRoot == root:
        cpy = "Not Copied"
    else:
        cpy = "Copied"
    print("Was the list copied? ")
    print(cpy)

if __name__ == "__main__":
    main()