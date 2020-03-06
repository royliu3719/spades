# --- Matplotlib Scatter Chart page.64
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)
y = np.sqrt(x) + 0.3 * np.random.rand(20)
p = np.poly1d([1, .0, 0.1])   # numpy.poLy1d 產生多項式 x^2 + 0.2 x + 0.1
f = np.poly1d(np.polyfit(x, y, 2))   # numpy.poLyfit 產生擬合的二階多項式係數
f1 = np.poly1d(np.polyfit(x, y, 3))   # numpy.poLyfit 產生擬合的二階多項式係數
plt.scatter(x, y, s=20, c=y, cmap='Blues', alpha=.6)
# plt.plot(x, y, 'ro')   # 畫紅點
plt.plot(x, f(x), color='m', label='f(x', linestyle='-.')
plt.plot(x, f1(x), color='m', label='f1(x', linestyle=':')
plt.plot(x, p(x), color='b', label='p(x', linestyle='--')
plt.legend(loc='best')
plt.show()


