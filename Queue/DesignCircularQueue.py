class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.front_idx = -1
        self.back_idx = -1
        self.capacity = k
    
    def display_elements(self):
        print("The elements in the Queue are ")
        print_str = ""
        # add the elements to the print string
        for i in range(self.capacity):
            print_str += str(self.q[i]) + " "
        print(print_str)

    def enQueue(self, value: int) -> bool:
        # if the queue is full return false
        if self.isFull():
            print("The queue is full..")
            return False
        # if the front index is negative, update its value to 0
        if self.front_idx == -1:
            self.front_idx = 0
        # increment the back index
        self.back_idx = (self.back_idx + 1) % self.capacity
        # update the queue value
        self.q[self.back_idx] = value
        return True

    def deQueue(self) -> bool:
        # if the queue is empty return false
        if self.front_idx == -1:
            print("The queue is empty..")
            return False
        self.q[self.front_idx] = None
        # if the front and back indices are the same reset the queue indices
        if self.front_idx == self.back_idx:
            self.front_idx = -1
            self.back_idx = -1
        else:
            # increment the front idx
            self.front_idx = (self.front_idx + 1) % self.capacity
        return True

    def Front(self) -> int:
        # if the front idx is -1 return -1 else the front value
        return -1 if self.front_idx == -1 else self.q[self.front_idx]

    def Rear(self) -> int:
        # if the rear idx is -1 return -1 else the back value
        return -1 if self.back_idx == -1 else self.q[self.back_idx]

    # check if queue is empty
    def isEmpty(self) -> bool:
        return self.front_idx == -1

    # check if queue is full
    def isFull(self) -> bool:
        return (self.back_idx + 1) % self.capacity == self.front_idx

def main():
    Queue = MyCircularQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.display_elements()
    Queue.deQueue()
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.enQueue(20)
    Queue.enQueue(10)
    Queue.display_elements()
    print("The front element of the queue is " + str(Queue.Front()))
    print("The rear element of the queue is " + str(Queue.Rear()))
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    Queue.deQueue()
    print("The front element of the queue is " + str(Queue.Front()))
    print("The rear element of the queue is " + str(Queue.Rear()))
    Queue.display_elements()


if __name__ == "__main__":
    main()