"""

Implement an algorithm to
determine if a string has all
unique characters.What
if you cannot use additional data structures?

"""


def Is_unique(s):
    return len(set(list(s))) == len(s)

print(Is_unique("an"))