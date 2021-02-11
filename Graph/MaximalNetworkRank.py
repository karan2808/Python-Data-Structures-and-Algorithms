from collections import Counter
class Solution:
    def maximalNetworkRank(self, n, roads):
        result = 0
        v = Counter()
        e = Counter()

        for i in roads:
            # count each vertex and also the edge between the vertices
            v[i[0]] += 1
            v[i[1]] += 1
            e[(i[0], i[1])] = True

        # n^2 complexity 
        for i in range(0, n):
            for j in range(i + 1, n):
                # add the count of vertices and subtract one since we count roads twice
                if e[(i, j)] or e[(j, i)]:
                    current = v[i] + v[j] - 1
                # just add the count of the vertices
                else:
                    current = v[i] + v[j]
                result = max(result, current)
        
        return result

def main():
    mySol = Solution()
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    print("The maximal network rank for roads " + str(roads) + " is " + str(mySol.maximalNetworkRank(n, roads)))

if __name__ == "__main__":
    main()