class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("banana")
    trie.insert("orange")
    trie.insert("grape")
    trie.insert("pear")

    print(trie.search("apple"))  # Output: True
    print(trie.search("banana"))  # Output: True
    print(trie.search("orange"))  # Output: True
    print(trie.search("grape"))  # Output: True
    print(trie.search("pear"))  # Output: True
    print(trie.search("pineapple"))  # Output: False

    print(trie.starts_with("app"))  # Output: True
    print(trie.starts_with("ban"))  # Output: True
    print(trie.starts_with("gr"))  # Output: True
    print(trie.starts_with("pe"))  # Output: True
    print(trie.starts_with("pin"))  # Output: False