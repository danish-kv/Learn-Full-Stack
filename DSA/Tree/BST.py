class BST:
    def __init__(self, key) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return print('Duplicate not allowed')
        
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    

    def search(self, data):
        if self.key is None:
            return print('BST is None')
        
        if self.key == data:
            return print('Fonud')
        
        if data < self.key:
            if self.lchild is not None:
                return self.lchild.search(data)
            else:
                return print("Not Found")
        else:
            if self.rchild is not None:
                return self.rchild.search(data)
            else:
                return print('Not Found')
    
    def conatin(self, data):
        curr = self
        while curr:
            if curr.key == data:
                return 'FOund '
            elif data < curr.key:
                curr = self.lchild
            else:
                curr = self.rchild
        return 'Not FOund'
    

    def preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preorder()
            
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()

        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()

        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')

            
    
    def remove(self, data, curr):
        if self.key is None:
            return print('Not FOund')
        
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.remove(data,curr)
            else:
                return print('Not Found')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.remove(data, curr)
            else:
                return print('Not Found')
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild - temp.rchild
                    temp = None
                    return
                self = None
                return temp
            
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key

            self.rchild = self.rchild.remove(node.key, curr)
            return self
        



arr = [12, 8, 3, 98, 45]
tree = BST(10)
for i in arr:
    tree.insert(i)

print(tree.search(8))
print(tree.search(10))
print('Pre Order')
tree.preorder()
print('\nIn order')
tree.inorder()
print('\nPost Order')
tree.postorder()
print()
tree.remove(10, tree.key)
print('After deletetion opretion')
tree.preorder()
print()
