"""
One Away: There
are
threetypes
of
edits that
can
be performed onstrings:insert a character,removea character, orreplacea character.Given
two
strings, write a function to check if they are one edit(orzero edits) away.
EXAMPLE
pale, pIe -> true
pales,pale -> true
pale,bale -> true
pale, bake -> false

"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # if abs(len(s) - len(t)) == 1 and ( not s or not t):
        #     return True
            
        if abs(len(s) - len(t)) > 1 or (not s and not t):
            return False
        # Defining largest and smaller strings
        shortS = s if len(s) <= len(t) else t
        longS  =  s  if len(s) > len(t) else t
        # Defining two pointers starting at zero
        index1 = 0 # index1 is associated with shortS
        index2 = 0  # index2 is associated with longS
        # defining a boolean flag, represents whether we found a single difference
        foundifference = False

        while index1 < len(shortS) and index2 < len(longS):
            # if the letters are different, if foundifference, we return false, otherwise, we set 
            # foundifference to True
            if shortS[index1] != longS[index2]:
                if foundifference:                  
                    return False
                foundifference = True
                # if the strings are same lengths, we increment both pointers
                if len(shortS) == len(longS):
                    index1 += 1 
                    index2 += 1
                else:
                    # if the strings have different lengths, we incrememt the pointer of the 
                    # the largest string
                    index2 += 1
            else:
                # if the letters at specifics indexes are the same, we increment both pointers 
                index1 += 1 
                index2 += 1
        # if after while loop, we still have a letter that is left, if previously found a difference(foundifference         #is True), we return False, otherwise we set foundifference to True
        
        if index1 < len(shortS) or index2 < len(longS):
            if foundifference: 
                return False
            foundifference = True
                
        return foundifference

    







def make_letter_counts_dict(str):
    """Return dict of letters and # of occurrences in phrase."""

    letter_counts = {}

    for letter in str:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts


def oneAway(str1,str2):
  A = {}
  B = {}
  A= make_letter_counts_dict(str1)
  print (A)
  B= make_letter_counts_dict(str2)
  print (B)

  count = 0
  for (key,value) in A.items():
    if not (key,value) in B.items():
        count += 1
    

  return count==1
  
  
  
print(oneAway("task", "take"))