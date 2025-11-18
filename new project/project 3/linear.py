import numpy as np

# Define matrices
A = np.array([[2, 3],
              [1, 4]])

B = np.array([[5, 2],
              [3, 1]])

# Matrix addition
print("A + B =\n", A + B)

# Matrix multiplication
print("A * B =\n", np.dot(A, B))

# Transpose
print("A^T =\n", A.T)

# Determinant
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# Inverse
inv_A = np.linalg.inv(A)
print("Inverse of A:\n", inv_A)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solving linear equations: Ax = b
b = np.array([8, 7])
x = np.linalg.solve(A, b)
print("Solution x:", x)