import numpy as np
from numpy.linalg import inv
a = np.array([[1,0.5,5],[2.3,2,3],[4,1,1.7]], dtype=np.float32)
b = np.array([[1,2,3]], dtype=np.float32)
x = np.matmul(inv(a), np.transpose(b))
print(x)