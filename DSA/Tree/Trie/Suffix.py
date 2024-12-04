class SuffixNode:
    def __init__(self) -> None:
        self.child = {}
        self.is_end = False


class SuffixTree:
    def __init__(self) -> None:
        self.root = SuffixNode()

    def insert(self, word):
        for i in range(len(word)):
            self.insert_helper(i, word)

    def insert_helper(self, i, word):
        node = self.root

        for j in range(i, len(word)):
            if word[j] not in node.child:
                node.child[word[j]] = SuffixNode()
            node = node.child[word[j]]
        node.is_end = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.child:
                return False
            node = node.child[i]
        
        return True
    
    def prefix_search(self, word):
        node = self.root
        for i in word:
            if i not in node.child:
                return []
            node = node.child[i]
        
        return self.prefix_search_helper(node, word)
    
    def prefix_search_helper(self, node, word):
        res = []
        if node.is_end:
            res.append(word)
        
        for char, child_node in node.child.items():
            res.extend(self.prefix_search_helper(child_node, char+word))

        return res
    
    def remove(self, word):
        self.remove_helper(self.root, word, 0)
    
    def remove_helper(self,node, word, index):
        if len(word) == index:
            node.is_end = False
            return
        
        letter = word[index]

        if letter not in node.child:
            return False
        
        child_node =  node.child[letter]
        self.remove_helper(child_node, word, index+1)

        if not child_node.child and not child_node.is_end:
            del child_node[letter]
        
        