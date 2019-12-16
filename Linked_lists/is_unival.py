# A tree is unival in x if and only if every node within the tree has the value x. Write a function that determines whether a given tree is unival.

#      1
#  1      1

#      1
#   1       1
# 2  2


class TreeNode:
    def __init__(self,x,left=None, right=None):
        self.val= x
        self.left = left
        self. right = right
    
    def isUnival(self):
        return self.isUnivalWithValue(self.val)
        
    def isUnivalWithValue(self, value):
        if self.val == None: 
            return False 
        # val != None is True here
        
        # if self.right == None and self.left == None:
        #     return True 
        
#         if self.left:
#                 if self.val != self.left.val:
#                     return False 
#         if self.right:
#                 if self.val != self.right.val:
#                     return False
#         if self.left and self.right:
#             if self.val == self.right.val == self.left.val:
#                 return True
        
        is_unival = self.val == value
        is_left_unival = self.left.isUnivalWithValue(value) if self.left else True
        is_right_unival = self.right.isUnivalWithValue(value) if self.right else True
        # print(value, self.val, is_unival, is_left_unival, is_right_unival)
        return is_left_unival and is_right_unival and is_unival
    
    def __str__(self):
        if self.left and self.right:
            return f"{self.val}\n{self.left.val} {self.right.val}"
        else:
            return f"{self.val}"
    
    
# Tree1 = TreeNode(1) #, TreeNode(1), TreeNode(1)
# print("Printing tree: \n", Tree1)

assert TreeNode(None).isUnival() == False
assert TreeNode(1).isUnival() == True
assert TreeNode(1, TreeNode(1), TreeNode(1)).isUnival() == True
assert TreeNode(1, TreeNode(1), TreeNode(2)).isUnival() == False
assert TreeNode(1, TreeNode(1), TreeNode(None)).isUnival() == False
assert TreeNode(None, TreeNode(None), TreeNode(None)).isUnival() == False
assert TreeNode(1, TreeNode(1)).isUnival() == True
assert TreeNode(1,TreeNode(1,TreeNode(2), TreeNode(3)), TreeNode(1,TreeNode(4),TreeNode(5))).isUnival() == False
print("All good.")