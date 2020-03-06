# --- 建立陣列 page.42
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

c = np.array([[[1,2], [3, 4]],[[5, 6],[7, 8]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)