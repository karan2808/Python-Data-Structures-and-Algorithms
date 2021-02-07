class Solution:
    def __init__(self, maxSize):
        # initialize an empty stack array, keep a track of stack size and top most element in the stack
        self.stackArr = [0 for i in range(maxSize)]
        self.stackSize = maxSize
        self.stackTop = 0

    # push an element on to stack if its not full
    def push(self, x):
        if self.stackTop < self.stackSize:
            self.stackArr[self.stackTop] = x
            self.stackTop += 1

    # pop an element from the top of the stack and return it, if empty return
    def pop(self):
        if self.stackTop:
            self.stackTop -= 1
            temp = self.stackArr[self.stackTop]
            return temp
        return -1
    
    # increment the bottom k elements of the stack by val
    def increment(self, k, val):
        for i in range(min(self.stackTop, k)):
            self.stackArr[i] += val

    # print the elements of the arr
    def printElements(self):
        for i in range(self.stackTop):
            print(self.stackArr[i])


def main():
    customArr = Solution(10)
    customArr.push(5)
    customArr.push(909)
    customArr.push(777)
    customArr.push(-2)
    customArr.push(0)
    customArr.push(9)
    customArr.push(55)
    print("The elements in the stack are ")
    customArr.printElements()
    x = customArr.pop()
    print("Popped element: " + str(x))
    x = customArr.pop()
    x = customArr.pop()
    x = customArr.pop()
    x = customArr.pop()
    x = customArr.pop()
    x = customArr.pop()
    print("The elements in the stack are ")
    customArr.printElements()

if __name__ == "__main__":
    main()