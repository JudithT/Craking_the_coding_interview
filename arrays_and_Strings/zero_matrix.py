"""
Zero
Matrix:
Write
an
algorithm such that
if
an element in
an
MxN
matrix
is
0,
its entire row andcolumn
are
set
to
O
"""




def zero_matrix(mat):
  n = len(mat)
  m = len(mat[0])
  zero_rows, zero_cols = [],[]
  
  if n == 0:
    return mat

  for r in range(n):
      for c in range(m):
        if mat[r][c] == 0:
          zero_cols.append(c)
          zero_rows.append(r)
          break

  for r in zero_rows:
      for c in range(m):
        mat[r][c]= 0

  for c in zero_cols:
      for r in range(n):
        mat[r][c]=0

  return mat


print(zero_matrix([[1,2,3],
                    [4,0,6],
                    [7,8,9]]))
