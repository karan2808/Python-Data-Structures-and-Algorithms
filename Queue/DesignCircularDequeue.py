class MyCircularDeque:
    def __init__(self, k):
        self.q = [None] * k
        self.front_idx = -1
        self.back_idx = -1
        self.capacity = k
    
    def display_elements(self):
        print("The elements in the Deque are ")
        print_str = ""
        # add the elements to the print string
        for i in range(self.capacity):
            print_str += str(self.q[i]) + " "
        print(print_str)
    
    def get_idx(self, idx):
        # if the index is negative, circle back
        if (idx < 0):
            return self.capacity + idx
        # else check from front
        return idx % self.capacity
    
    def insert_front(self, val):
        if self.isFull():
            print("The dequeue is full.")
            return
        # if its the first element, increment front and rear
        if (self.front_idx == -1 and self.back_idx == -1):
            self.front_idx = 0
            self.back_idx = 0
        else:
            # decrement the front index
            self.front_idx = self.get_idx(self.front_idx - 1)
        # insert element in the front index
        self.q[self.front_idx] = val
        print("Inserted Element..")
    
    def insert_last(self, val):
        if (self.isFull()):
            print("Deque is full..")
            return
        if (self.front_idx == -1 and self.back_idx == -1):
            self.front_idx = self.back_idx = -1
        else:
            self.back_idx = self.get_idx(self.back_idx + 1)
        # insert the element in the back of the dequeue
        self.q[self.back_idx] = val
        print("Inserted the element")
    
    def delete_front(self):
        if (self.isEmpty()):
            print("The deque is empty..")
            return
        self.q[self.front_idx] = None
        if (self.front_idx == self.back_idx):
            self.front_idx = self.back_idx = -1
        else:
            self.front_idx = self.get_idx(self.front_idx + 1)
        print("Deleted element from front..")
    
    def delete_rear(self):
        if (self.isEmpty()):
            print("The deque is empty")
        # delete the rear element
        self.q[self.back_idx] = None
        # if the front and back indices are the same
        if (self.front_idx == self.back_idx):
            self.front_idx = self.back_idx = -1
        else:
            self.back_idx = self.get_idx(self.back_idx - 1)
        print("Element deleted from rear..")
    
    def get_front(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front_idx]

    def get_back(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.back_idx]
    
    # check whether dequeue is empty
    def isEmpty(self):
        if (self.front_idx == -1 and self.back_idx == -1):
            return True
        else:
            return False

    def isFull(self):
        return (self.back_idx == self.capacity - 1 and self.front_idx == 0) or (self.back_idx < self.front_idx and self.back_idx + 1 == self.front_idx)
    
def main():
    deque = MyCircularDeque(10)
    deque.insert_front(20)
    deque.insert_front(10)
    deque.insert_last(8)
    deque.display_elements()

if __name__ == "__main__":
    main()