# First Common ancestor: Design an algorithm and write code to find te first common 
# ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data
# structure. Note: This is not necessarily a binary search tree. 

class TreeNode:
    def __init__(self,x):
        self.val = x 
        self.left = None
        self.right = None 

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if not root:
            return None

        def _helper(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = _helper(node.left)
            right = _helper(node.right)
            
            if not left:
                return right
            if not right:
                return left
            return node

        return _helper(root)