
class Trie(object):
    size = 26
    min_element = ord('a')
    
    class TrieNode(object):
        def __init__(self, value=None):
            self.value = value
            self.children = [None] * Trie.size

    def __init__(self):
        self.root = self.TrieNode()
            
    def __setitem__(self, word, value):
        node = self.root
        for letter in word:
            ix = ord(letter) - self.min_element
            assert ix < self.size

            print 'letter', letter
            child = node.children[ix]
            if child:
                node = child
            else:
                node.children[ix] = self.TrieNode()
                node = node.children[ix]
        node.value = value

    def __getitem__(self, word):
        node = self.root
        for letter in word:
            ix = ord(letter) - self.min_element
            assert ix < self.size
            node = node.children[ix]
            if not node:
                raise KeyError
        return node.value

    def __contains__(self, word):
        node = self.root
        for letter in word:
            ix = ord(letter) - self.min_element
            assert ix < self.size
            node = node.children[ix]
            if not node:
                return False
        return node.value is not None
            
            
                
            
                
