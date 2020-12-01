"""
Lists of Depths: 
Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth(e.g, if you have a tree with depth D, you will have D linked lists)
"""

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None 
        self.next = None 
    
    def list_of_depths(self):
        if not root: return root
        q = [root]
        while q: 
            q_size = len(q)
            for i in range(q_size):
                node = q.pop(0)
                if i < q_size - 1:
                    node.next = q[0]
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root




    class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = [root]
          
        while q:
            q_size = len(q)
            # not quite sure why 
            for i in range(q_size):
                node = q.pop(0)
            # not quite sure why 
                if i < q_size -1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root



