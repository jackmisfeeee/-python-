# 1、计算字符串str1切片的结果
"""
str1="Python is amazing!"
P    y     t   h    o    n         i    s        a     m     a    z   i   n   g   !
0    1     2   3    4    5    6    7    8    9   10    11    12   13  14  15  16  17
-19 -18  -17  -16  -15  -14  -13  -12  -10  -9   -8    -7    -6   -5  -4  -3  -2  -1
str1[::]  #全切
str1[0:18]      # Python is amazing!
str1[1:15]      # ython is amazi
str1[1:17:3]    # yoiazg
str1[-1:]       # ！
str1[-10:-2]    # s amazin
str1[:-2:-1]    # !
str1[::-1]      # !gnizama si nohtyP
str1[:-5:-1]    # !gni
str1[::0]       # 切片步长不能为0 值错误
"""

# 2、使用while循环输出字符串当中的每个元素“路漫漫其修远兮,吾将上下而求索”。

str1 = "路漫漫其修远兮，吾将上下而求索"
# 初始化下标为0
subscript = 0
# 当下标小于字符串长度执行以下代码
while subscript < len(str1):
    # 输出字符串中下标为subscript值的元素，以空字符结尾
    print(str1[subscript], end='')
    # 下标值加一 依次循环 直到输出最后一个元素 结束循环
    subscript += 1

# 3、统计字符串“Learning will never stop, never learned knowledge.”的长度。
print()
str2 = "Learning will never stop, never learned knowledge."
# 初始化统计长度
length = 0
# 调用len()函数计算字符串长度并传递给length
length = len(str2)
# 输出字符串长度
print(f'字符串长度为:{length}')
# 4、去除字符串当中的空格 "Hello, world! This is a test."，并保存为列表。

str3 = "Hello, world! This is a test."
# 将字符串中的空格替换成空字符 达到去除空格操作，再链式转换为列表并存入一个列表变量中
list1 = str3.replace(' ', '').split()
# 输出查看结果
print(list1)
# 5、写一个程序，输入五个数字，计算五个数字的累加和，如果用户输入不是数字请让用户重新输入。

# ---方案1：使用数据容器接收来进行累加
# 创建一个空数字列表用于接收用户输入内容
number_list = []
# 创建一个中间变量来将用户输入内容传入列表
t = 0
# 初始化计数器
c = 0

# 5次输入
while c < 5:
    # 使用try-except语句来判断用户输入内容
    try:
        # 接收用户输入内容 转换成浮点类型
        t = float(input(f"请输入第{c + 1}个数字: "))
        # 将输入内容传递到列表：
        number_list.append(t)
        # 计数器值+1
        c += 1
    except ValueError:
        # 如果输入内容不是数字，提示数值类型错误，并重新返回try中输入
        print('输入无效，请输入一个有效的数字：')
# 初始化五个数字的和
sum_of_nums = 0
# 累加五个数字
for i in range(0, len(number_list)):
    sum_of_nums += number_list[i]
# 输出累加和
print(f"五个数字累加的和为：{sum_of_nums}")

print('-------------------------------------------------------------------------------------------------')

# ---方案2：使用基本逻辑实现
# 初始化累加和为 0
total = 0
# 初始化计数器为 0
count = 0

while count < 5:
    try:
        # 获取用户输入
        num = input(f"请输入第 {count + 1} 个数字: ")
        # 将输入转换为浮点数
        num = float(num)
        # 累加输入的数字
        total += num
        # 计数器加 1
        count += 1
    except ValueError:
        # 如果输入不是数字，提示用户重新输入
        print("输入无效，请输入一个有效的数字。")

# 输出累加和
print(f"这五个数字的累加和是: {total}")
