# input 函数
# 作用: input() 函数是 Python的内置函数，用于从用户处获取输入信息。
# 语法：input(prompt)
# Prompt(可选参数) :  用于指定提示用户输入的消息,让用户知道他们需要输入什么,它是一个字符串类型的参数。

# name = input('请输入你的名字：')
# print(f'老师的名字是:{name}')

# 如果之间按下回车键，那么input接收到的就是空字符串

# 注意：如果在控制台不输入内容，input函数会永远等待输入，不会执行接下来的代码。

# age = input()
# print(f'年龄是：{age}')
# 一般我们都是会去写提示信息

# input会把用户输入的所有内容转换为字符串，并作为 input 函数的返回值。
# num = input('请输入：')
# print(num, type(num))

# 如果需要其他类型的数据，可以使用类型转换函数进行转换。
# int()、float()、bool()、str()都是python内置函数。
# int() 用于将一个值转换为整型。
a = int(1.88)  # 丢掉小数，也不考虑四舍五入
print(a, type(a))

a = int(True)
print(a, type(a))

a = int('100')
print(a, type(a))

# 1 <class 'int'>
# 1 <class 'int'>
# 100 <class 'int'>

# int()不能转换字符串里非纯数字
print(int(12.3))  # 能转

# print(int('12.3'))  # 转不了
# ValueError: invalid literal for int() with base 10: '12.3'

# float()用于将一个值转换为浮点型。

a = float(10)  # 10.0
print(a, type(a))

a = float(True)  # 1.0
print(a, type(a))

a = float('100')  # 100.0
print(a, type(a))

a = float('10.77')  # 10.77
print(a, type(a))
# float()可以转换字符串里面是数字。

# a = float('一百')
# print(a, type(a))
# ValueError: could not convert string to float: '一百'

# bool()用于将一个值转换为布尔值（查看数据的布尔值）。
print(bool(10))  # True
print(bool(0))  # False

# str()用于将一个值转换为字符串型。
a = str(10)  # '10'
print(a, type(a))

a = str(10.88)  # '10.88'
print(a, type(a))

a = str(True)  # 'True'
print(a, type(a))

# 注意：
# int()内的参数可以是数值类型、但是把字符串转换为整型，字符串里面必须是整数。
# float()内的参数可以是数值类型、但是把字符串转换为浮点型，字符串里面必须是数字。
# str()不限制类型。
