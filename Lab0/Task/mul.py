def mul(A, B):
  """
  return the product of the matrix A by  the matrix B
  returns the empty list [] if the matrix dimensions
  are not consistent for multiplication
  """
  # function body
  if (len(A[0]) != len(B)):
    return []
  rows_A, columns_A = len(A), len(A[0])
  rows_B, columns_B = len(B), len(B[0])

  result = [[0] * columns_B for _ in range(rows_A)]

  for i in range(rows_A):
    for j in range(columns_B):
      for k in range(columns_A):
        result[i][j] +=A[i][k]*B[k][j]
  return result
