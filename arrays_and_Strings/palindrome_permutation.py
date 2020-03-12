"""
 palindrome permutation:
Given a string, write a function to check if it is a permutation of a palindrome. A aplindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

 Example: Tact Coa
 Output: True( Permutation: "taco cat", "atco cta", etc)

"""

def is_palindrome_permutation(string):
  counter = Counter()
  for letter in string.replace(" ", ""):
    counter[letter] += 1
  #return sum([count % 2 for count in counter.values()]) < 2
  odd_counts = 0
  for count in counter.values():
    odd_counts += count % 2
    if odd_counts > 1:
      return False
  return True

# second approach 

def palindrome_permutation(s):
    container = set()
    arr = list(s)
    alphabet ="abcdefghijklmnopqrstuwxyz"

    for char in s:
      if char  in  container:
          if char in alphabet:
              container.remove(char)
          else:
              container.add(char)

    return len(container) <=1 


print(palindrome_permutation("tact coa"))