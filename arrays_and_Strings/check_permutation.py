"""
Given two strings, write a method to decide if one is a permutation if the other
"""

def check_permutation(s1,s2):
    arr1=list(s1)
    arr2 = list(s2)
 
    if len(s1)!= len(s2):
        return False
    for char in arr1:
        if arr1.count(char) != arr2.count(char):
          return False
    
    return True


print(check_permutation("love", "lova"))