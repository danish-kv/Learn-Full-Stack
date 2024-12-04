class PrefixNode:
    def __init__(self) -> None:
        self.child = {}
        self.is_end = False


class PrefixTree:
    def __init__(self) -> None:
        self.root = PrefixNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.child:
                node.child[i] = PrefixNode()
            node = node.child[i]
        node.is_end = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.child:
                return False
            node = node.child[i]
        return node.is_end
    
    def prefix_search(self, word):
        node = self.root
        for i in word:
            if i not in node.child:
                return []
            node = node.child
        
        return self.prefix_search_helper(node, word)
    
    def prefix_search_helper(self, node, word):
        res = []
        if node.is_end:
            res.append(word)
        
        for char, child_node in node.child.items():
            res.extend(self.prefix_search_helper(child_node, word+char))
        
        return res
    

    def remove(self, word):
        return self.remove_helper(self.root, word, 0)
    
    def remove_helper(self, node, word, index):
        if len(word) == index:
            node.is_end = False
            return
        
        letter = word[index]
        if letter not in node.child:
            return
        
        child_node = node.child[letter]
        self.remove_helper(child_node, word, index+1)

        if not child_node.child and not child_node.is_end:
            del child_node[letter]
            
    

