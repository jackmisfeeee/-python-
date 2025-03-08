# 成员运算符 (判断是不是它的成员)
# 成员运算符包括两种：in 、not in    翻译：在....里面和不在....里面
# 作用：用于判断一个对象是否包含另一个对象，返回值为布尔类型。
# in：如果一个对象在指定的对象中存在，则返回 True，否则返回 False。
# not in：如果一个对象不在指定的对象中存在，则返回 True，否则返回 False。
print('a' in 'abc')  # Ture
print('d' in 'abc')  # False

print('a' not in 'abc')  # False
print('d' not in 'abc')  # Ture

print('st' in 'str1')  # Ture
print('st' in 'sr1t')  # False 'st'整体

# 注意事项：
# 数值类型不能使用成员运算符（会报错），成员运算符可用于字符串、列表、元组等。
# 1 in 123

# 'abcdef' ，字符串是一个容器类型
# 'a' in 'abcdef'

# 身份运算符
# 身份运算符包括两种：is 、 is not
# 作用：用于比较两个对象的内存地址是否相同,即它们是否是内存中的同一个对象，返回值为布尔类型。
# is:判断左右两个对象的内存地址是否相等。如果两个对象指向的是同一内存地址，则返回True,否则返回False。
# is not:判断左右两个对象的内存地址是否不相等。如果两个对象指向的不是同一内存地址，则返回True,否则返回False。
name = '王五'

number1 = 1
number2 = number1
print(number1 is number2)  # True
print(number1 is not number2)  # False

number3 = 2
print(number3 is number1)  # False
print(number3 is number2)  # False

print(number3 is not number1)  # True
print(number3 is not number2)  # True

# id()函数用于获取对象的“身份标识符”，也就是该对象在内存中的地址。
print(id(number1))
print(id(number2))
print(id(number3))
# 140727752201904
# 140727752201904
# 140727752201936