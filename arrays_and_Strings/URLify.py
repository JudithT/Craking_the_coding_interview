"""
URLify:
Write a
method to
replace
all
spaces
in
a string with
'%20:
You
may assume
that the
stringhas sufficient space
at
the
end
to hold
the
additional characters,
andthat
you are given
the
truelength
of
the
string.(Note:
If
implementing
in
Java, please use acharacterarray so
that
you canperform this operation
in
place.)
EXAMPLE
Input: Mr
John
Smith
J
13
Output: Mr%20J
ohn%20Smith
Hints
 
53,
7
78
9


"""

def URLify(s):
    # strip will remove the trailing spaces
    return s.strip().replace(" ", "%20")

print(URLify("MR John Smith  "))