class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode):
        if root == None:
            return True
        def high(node):
            if node == None:
                return 0
            return max(high(node.left), high(node.right)) + 1
        l = high(root.left)
        r = high(root.right)
        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)