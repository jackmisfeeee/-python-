# input()函数 x=input(prompt) ---变量 = 输入函数(提示词可有可无，但有对用户友好) = 赋值符 从控制台输入字符串赋值到变量 因此默认str类型
"""
name = input('请输入你的名字：')
sex = input('请输入你的性别：')
age = input('请输入你的年龄：')
Tel = input('请输入你的电话号码：')
address = input('请输入你的地址：')
print(name, sex, age, Tel, address)
"""
# ----------------------------------------------------------
"""
# 类型转换：
number = input('请输入一个数字')
number2 = input('请输入一个数字')
print(number, number2)  # 直接输出两个数字
print(number + number2)  # input("prompt") 函数存放的类型是str 因此直接拼接
print(type(number))  # 检测变量number内存储的数据类型
# 将类型转换：
# 1.在输入时复合转换：
num = int(input('请重新输入一个数字'))
num2 = int(input('请重新输入一个数字'))
# 此时num 和num2中存储的数据被int()函数转换成整型
print(num + num2)   # 做加法运算
print(type(num))    # 检测此时num类型是否转换为整型
"""
# ----------------------------------------------------------
"""
# 2.在定义后转换：
num = input("输入一个数字")
num2 = input("输入一个数字")
# 将类型强制转换后赋值回变量
num = int(num)
num2 = int(num2)
print(num + num2)   # 求和
print(type(num))    # 验证此时num类型
"""
# ----------------------------------------------------------
# 3.在输出时执行转换：
num = input("输入一个数字")
num2 = input("输入一个数字")
print(int(num) + int(num2))  # 将类型从str-->int 并且做加法后输出结果
print(type(num))    # 检测此时num类型
# 显然 此时num依然是str类型 ，类型转换在上一步产生，并伴随消失，并没改变全局的类型
