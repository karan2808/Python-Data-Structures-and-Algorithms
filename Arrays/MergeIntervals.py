class Solution:
    def merge(self, intervals):
        sz = len(intervals)
        result = []
        if (sz == 0):
            return result

        # sort the intervals in ascending order of first element
        sorted(intervals, key=lambda x: x[0])

        # store the first interval into result
        result.append(intervals[0])

        currentInterval = intervals[0]

        # use an idx to iterate over intervals
        idx = 0

        for interval in intervals:
            # get current intervals end to compare it to interval
            currEnd = currentInterval[1]
            nextBegin = interval[0]
            nextEnd = interval[1]
            # if the next interval start is less than current intervals end, there is overlap
            if currEnd >= nextBegin:
                currentInterval[1] = max(currEnd, nextEnd)
                result[idx][1] = currentInterval[1]
            else:
                # set the current interval to interval since there is no overlap
                currentInterval = interval
                result.append(currentInterval)
                idx += 1
        result


def main():
    mySol = Solution()
    nums = [[1, 3], [2, 6], [8, 10], [15, 18], [16, 21]]
    result = mySol.merge(nums)
    print("Merged intervals for the given intervals " +
          str(nums) + " are " + str(result))


if __name__ == "__main__":
    main()
