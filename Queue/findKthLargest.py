import heapq 

class KthLargest:
    def __init__(self, nums):
        self.nums = nums
    
    def findKthLargest(self, k):
        # heapify the given list
        heapq.heapify(self.nums)
        kthLargest = 0
        # pop len - k + 1 elements from back since smallest elements will be stored in the back
        for i in range(len(self.nums) - k + 1):
            kthLargest = heapq.heappop(self.nums)
        return kthLargest
    
def main():
    nums = [1, -9, 3, 2, 8]
    KL = KthLargest(nums)
    print("The 5th largest element is " + str(KL.findKthLargest(5)))
    print("The 1st largest element is " + str(KL.findKthLargest(1)))
    print("The 2nd largest element is " + str(KL.findKthLargest(2)))

if __name__ == "__main__":
    main()
        