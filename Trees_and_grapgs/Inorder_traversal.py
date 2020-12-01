# Inorder Traversal ; Left - > root -> right 

def inorder_traversal(root):
    if not root: return []
    stack = []
    res = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    return res




class Solution:
#     def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
#         if not root:
#             return []
#         stack = list()
#         output = list()
#         while stack or root:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 node = stack.pop()
#                 output.append(node.val)
#                 root = node.right
#         return output   










        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         # 1.Print Left Node
#         # 2. Print parent 
#         # 3. print right Node
#             if root:
#                 self.inorderTraversal(root.left)
#                 print(root.val, end = ' ')
#                 self.inorderTraversal(root.right)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [], []
        curr = root
        while(curr is not None or len(stack)):
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res 
        

# THE SOLUTION BELOW WORKS TOO
                        
# class Solution:
#     def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
#         if not root:
#             return []
#         stack = list()
#         output = list()
#         while stack or root:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 node = stack.pop()
#                 output.append(node.val)
#                 root = node.right
#         return output   
        
        
        
        
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         ans = []
        
#         # In-order traversal: left->root->right
        
#         def dfs(node):
#             if not node: return
#             dfs(node.left)
#             ans.append(node.val)
#             dfs(node.right)
            
#         dfs(root)
#         return ans
        
        
        

         