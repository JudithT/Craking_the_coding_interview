def postorder_traversal(root):


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]



class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root,],[]
        
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        print(res)
        return res[::-1]