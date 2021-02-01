class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        self.front = None

    def push(self, x):
        if len(self.stk1) == 0:
            self.front = x

        # empty stack 1 into stack 2
        while len(self.stk1):
            y = self.stk1.pop()
            self.stk2.append(y)

        # append x to stack 1 and empty stack 2 into stack 1 so that the new element is added at the back
        self.stk1.append(x)
        while len(self.stk2):
            y = self.stk2.pop()
            self.stk1.append(y)

    # pop the top element
    def pop(self):
        self.front = self.stk1.pop()
        return self.front

    # get the top element
    def peek(self):
        self.front = self.stk1[-1]
        return self.front

    def empty(self):
        return len(self.stk1) == 0


def main():
    myQ = MyQueue()
    myQ.push(5)
    myQ.push(10)
    myQ.push(7)
    print("Queue top is " + str(myQ.peek()))
    myQ.pop()
    print("After popping an element queue top is " + str(myQ.peek()))

if __name__ == "__main__":
    main()
