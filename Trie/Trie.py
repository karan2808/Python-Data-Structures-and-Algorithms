class TrieNode:
    def __init__(self):
        # links from current node, initially set to None
        self.links = {}
        # is the current node the end of word
        self.isEow = False

    def setEnd(self):
        self.isEow = True

    def put(self, c, node):
        self.links[c] = node

    def get(self, c):
        return self.links[c]

    def containsKey(self, c):
        if c not in self.links.keys():
            return False
        return True

    def isEnd(self):
        return self.isEow


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # get current node
        curr = self.root
        # go through the characters
        for c in word:
            # if key not found insert it
            if not curr.containsKey(c):
                curr.put(c, TrieNode())
            # go to next node
            curr = curr.get(c)
        curr.setEnd()

    # search the prefix node
    def searchPrefix(self, word):
        curr = self.root
        for c in word:
            # if key not found, return NULL
            if not curr.containsKey(c):
                return None
            # go to next link
            curr = curr.get(c)
        return curr

    # search for the given word
    def search(self, word):
        curr = self.searchPrefix(word)
        if curr != None and curr.isEnd():
            return True
        return False

    def startsWith(self, prefix):
        if self.searchPrefix(prefix) != None:
            return True
        return False


def main():
    t = Trie()
    t.insert("hello world")
    print(t.startsWith("hello"))
    print(t.startsWith("yo"))
    print(t.search("hello world"))
    print(t.search("hello"))


if __name__ == "__main__":
    main()
