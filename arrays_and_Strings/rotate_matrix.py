"""
Rotate
Matrix:
Given
an
image represented by
an
NxN
matrix,where
each
pixel in the image
is
4bytes,writea method to rotate the image by
90
degrees.
(an
you do this in
place?
"""

def rotate_matrix(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
      for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


print(rotate_matrix([[1,2,3],
                     [4,5,6],
                     [7,8,9]]))




def rotate_matrix_inplace(mat):
  if len(mat)== 0:
    return

  if len(mat) == 1
     return matrix 

  lenr= len(mat)
  lenc = len(mat[0])

  new_matrix = [row[:]for row in mat]

  for row in range(lenr):
       new_matrix.append(mat[row][col]
