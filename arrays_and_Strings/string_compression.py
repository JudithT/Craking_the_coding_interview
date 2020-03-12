"""
String Compression: Implement a method to perform basic string compression using the counts
of
repeated characters.
For
example, the string
aabcccccaaa
would become a2b1c5a3.
If
thecompressedstring would
not
become smaller than the original string, your method should returnthe originalstring.
You
can
assume the string
has
only uppercase and lowercase letters
(a
-
z).
Hints:
92,
11
0
"""

def string_compression(s):
  result = ""
  count = 0
  arr = list(s)

  for i in range(len(arr)-1):
     if arr[i] == arr[i+1]:
       count += 1
     else:
        result += arr[i]+ str(count)
        count =1
  result += arr[i]+ str(count)

  if(len(result) >= len(s)):
    return s
  else:
    return result

  return result


print(string_compression("aaaabbbcnnmmm"))