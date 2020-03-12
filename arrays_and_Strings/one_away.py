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