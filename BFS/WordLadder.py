class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # make a queue for bfs
        queue = []

        # make a set for quick access
        s = set()
        for word in wordList:
            s.add(word)
        
        if endWord not in s:
            return 0
        
        # do a bfs
        queue.append(beginWord)
        depth = 0

        while len(queue):
            # increment depth and get queue size
            depth += 1
            sz = len(queue)

            for k in range(sz):
                current = queue.pop(0)
                # for each character in the current word
                for i in range(len(current)):
                    # store the current string to revert it back after changes
                    temp = current
                    for j in range(26):
                        # change each character
                        current = current[:i] + chr(ord('a') + j) + current[i+1:]
                        # if we get the same word again continue
                        if current == temp:
                            continue

                        # if current is end word return the depth 
                        if current == endWord:
                            return depth + 1
                        
                        # if current word is in the dictionary, append it to queue and discard it from the dictionary
                        if current in s:
                            queue.append(current)
                            s.discard(current)
                    
                    # revert the changes done to current
                    current = temp

        return 0

def main():
    startWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    mySol = Solution()
    print("The transformations required for start word hit, end word cog and the word list:")
    print(wordList)
    print("are: " + str(mySol.ladderLength(startWord, endWord, wordList)))

if __name__ == "__main__":
    main()
