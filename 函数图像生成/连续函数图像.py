import matplotlib.pyplot as plt
import numpy as np

# 生成 x 值，在 -10 到 10 之间取 400 个点
x = np.linspace(-10, 10, 1000)

# 计算对应的 y 值
y = x ** 2

# 绘制图像
plt.plot(x, y)

# 添加标题和坐标轴标签
plt.title('Function Graph: y = x^2')
plt.xlabel('x')
plt.ylabel('y')

# 显示网格线
plt.grid(True)

# 显示图像
plt.show()