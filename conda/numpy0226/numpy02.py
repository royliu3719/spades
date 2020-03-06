# --- 指定陣列的資料型態 page.43
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype)

a = np.array([1, 2, 3, 4], np.int64)
print(a)
print(a.dtype)

a = np.array([1, 2, 3, 4], dtype=float)
print(a)
print(a.dtype)

a = np.array([1, 2, 3, 4], dtype=complex)
print(a)
print(a.dtype)

b = np.array(a, dtype=float, copy=True)
print(b)
print(b.dtype)