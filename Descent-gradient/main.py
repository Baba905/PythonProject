import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
B = A.T
C= A.dot(B)
print(A.shape)
print(B.shape)
print(C)