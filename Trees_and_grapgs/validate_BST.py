class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.right = right
        self.left = left 

class Solution:

    def validate(self, root, lowerlimit = float('-inf'), upperlimit = float('inf')):
        if not root:
            return True
        if root.val <= lowerlimit or root.val >= upperlimit:
            return False

        if not self.validate(root.left, lowerlimit, root.val):
            return False
        not self.validate(root.right, root.val, upperlimit):
            return False
        return True 



    def isValidate(self, root):
        return self.validate(root)
