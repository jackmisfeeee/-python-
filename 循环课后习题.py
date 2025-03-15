# 例1：构成无限循环，用户输入stop，停止循环。
while 1:
    ass = input()
    if ass == 'stop':
        break

# 例2：用while循环计算1到100的数字和，直到和大于等于1000时停止。
i = 1
s = 0
while i <= 100:
    s += i
    print(s)
    if s == 1000:
        break

# 例3：输出 5 行星号（*）的图形，形状如下：
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()
# 例4：输入一个字符串，使用for循环来统计一个字符串中o字符的出现次数。
string = input('请输入一个字符串：')
s = 0
for i in string:
    if i == 'o':
        s += 1
print(f"你输入的字符串中'o'出现了{s}次")
# 例5：输出1到10的阶乘。
s = 1
for i in range(1, 11, 1):
    s *= i
print(f"10！={s}")
