class MinStack:
    def __init__(self):
        self.regStack = []
        self.minStack = []
    
    # if the current element is less than minstack top or if minstack is empty, append the element to min stack
    def push(self, x):
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        self.regStack.append(x)

    # get the top element
    def top(self):
        return self.regStack[-1]

    # get the min value
    def getMin(self):
        return self.minStack[-1]


def main():
    mStack = MinStack()
    mStack.push(4)
    mStack.push(-1)
    mStack.push(-5)
    mStack.push(10)
    mStack.push(20)
    print("After pushing elements 4, -1, -5, 10, 20 elements in minstack are ")
    print(mStack.minStack)
    print("Min element is " + str(mStack.getMin()))


if __name__ == "__main__":
    main()