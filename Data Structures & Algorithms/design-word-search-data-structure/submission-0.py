class TrieNode:
    def  __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(curr, c):
            if c == len(word):
                return curr.endOfWord
            if word[c] == ".":
                for node in curr.children.values():
                    if dfs(node, c+1):
                        return True
                return False
            else:
                if word[c] not in curr.children:
                    return False
                else:
                    return dfs(curr.children[word[c]], c+1)
        curr = self.root
        return dfs(curr, 0)
        
