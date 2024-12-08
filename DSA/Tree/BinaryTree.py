class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if not current.lchild:
                current.lchild = new_node
                return
            else:
                queue.append(current.lchild)
            if not current.rchild:
                current.rchild = new_node
                return
            else:
                queue.append(current.rchild)
    

    def search(self, data):
        if not self.root:
            return 
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.key == data:
                return True
            
            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)
                
        return False
