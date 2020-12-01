"""
Given a sorted (increasing order) array with unique integer elements. write an algorithm
to create a binary search tree with minimal height

"""

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left  = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


def minimalTree(arr, start, end):
    if start > end:
        return ''
    mid = (end + start)// 2
    root = TreeNode(arr[mid])
    root.right = minimalTree(arr, mid + 1, end )
    root.left =  minimalTree(arr, start, mid -1 )
    return root 

def initiateArrayToBinary(arr):
    return minimalTree(arr, 0, len(arr) - 1)

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(initiateArrayToBinary(testArray))