class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def inorder ( self ) :
       if self.left :
           self.left.inorder ()
       print ( self.data, end= ' ' ) ,
       if self.right :
           self.right.inorder ()

class Solution:
    def invertTree(self, root):
       if root == None:
           return
       root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
       return root
if __name__ == '__main__':
    Tree = Node(10)
    Tree.left = Node(20)
    Tree.right = Node(30)
    Tree.left.left = Node(40)
    Tree.right.right = Node(50)
    print('Initial Tree :',end = ' ' )
    Tree.PrintTree()
    Solution().invertTree(root=Tree)
    print('\nInverted Tree :', end=' ')
    Tree.PrintTree()
