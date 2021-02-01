class MyStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        # push x onto the queue
        self.q.append(x)
        # after appending to the queue, the element should come first
        for i in range(len(self.q) - 1):
            # push back the initial elements to the back of the queue
            self.q.append(self.q[0])
            # pop the initial elements
            self.q.pop(0)

    # remove and get the top element of the stack
    def pop(self):
        return self.q.pop(0)

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

    def printS(self):
        S = ""
        for i in range(len(self.q)):
            S += str(self.q[i]) + " "
        print(S)


def main():
    stack = MyStack()
    stack.push(5)
    stack.push(10)
    stack.push(50)
    stack.push(-1)
    print("Elements of the stack are ")
    stack.printS()
    print("Stack top is " + str(stack.top()))
    print("Pop top element " + str(stack.pop()))
    print("After popping top element, elements of the stack are ")
    stack.printS()


if __name__ == "__main__":
    main()
