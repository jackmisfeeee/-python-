import matplotlib.pyplot as plt
import numpy as np

# 生成 n 的值，这里假设 n 从 1 到 10
n = np.arange(1, 11)

# 计算 y 的值
# a：此处更改函数表达式
# y = (-1) ** (n - 1)
y = ((n ^ (2 - 1)) - 1) / (n - 1)
# 绘制图像
plt.stem(n, y)
plt.xlabel('n')
# a：同步list8更改
# plt.ylabel('y = (-1)^(n - 1)')
plt.ylabel('y = ((n^(2-1))-1) / (n-1)')
# a:同上
plt.title('Graph of y = ((n^(2-1))-1) / (n-1)')
plt.show()
