import matplotlib.pyplot as plt
import numpy as np

# 生成更密集的 n 值，这里在 1 到 10 之间取 1000 个点
n = np.linspace(1, 10, 1000)

# 计算近似的 y 值，利用取整函数模拟 (-1) 的幂次
y = (-1) ** (np.floor(n - 1).astype(int))

# 绘制图像
plt.plot(n, y)
plt.xlabel('n')
plt.ylabel('y = (-1)^(n - 1) (approximate continuous)')
plt.title('Graph of Approximate Continuous y = (-1)^(n - 1)')
plt.grid(True)
plt.show()