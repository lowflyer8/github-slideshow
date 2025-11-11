class node:
    def __init__(self,key):
        self.key, self.left, self.right, = key , None ,None
        
class bst:
    def insert(self,root,key):
        if root is None:
            return node(key)
        if key < root.key:
            root.left = self.insert(root.left ,key)
        elif key>root.key:
            root.right = self.insert(root.right,key)
        return root
    
    def search(self,root,key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left ,key)
        else:
            return self.search(root.right , key)
        
    def inorder(self,root):
        return [] if not root else self.inorder(root.left) + [root.key] + self.inorder(root.right)
    
    def preorder(self,root):
        return [] if not root else [root.key] + self.preorder(root.left) + self.preorder(root.right)
    
    def postorder(self,root):
        return [] if not root else self.postorder(root.left) + self.postorder(root.right) + [root.key]
    
    def minvaluenode(self,node):
        while node.left:
            node = node.left
        return node
    
    def delete(self,root,key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left , key)
        elif key > root.key:
            root.right = self.delete(root.right , key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minvaluenode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root
    
bst = bst()
root = None

for key in [50,30,20,40,70,60,80]:
    root = bst.insert(root,key)
    
print("inorder transversal:", bst.inorder(root))
print("preorder transversal:", bst.preorder(root))
print("postorder transversal", bst.postorder(root))
print("search 40:","found" if bst.search(root,40) else "not found")

root = bst.delete(root, 20 )
print("after deleting 20 (inorder):" , bst.inorder(root))