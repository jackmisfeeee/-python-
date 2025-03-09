# 0、None、空字符串、空列表、空元组、空字典、空集合等布尔值为False，其他类型数据的布尔值为True。
# False的本质是0，True的本质是1。

# 优先级： not > and > or

# 1） not  (逻辑非)
# 作用：用于对布尔值取反，并返回一个新的布尔值。
# 它是一个元运算符。
print(not (1 > 2))  # not False-->True
print(not True)  # False

x = 10
print(not (x - 5) > 0)  # False 优先级：（）>比较运算符 > not

print(not 123)  # False
print(not -123)  # False -123布尔值也是True

print(not "")  # True
print(not " ")  # False

#  2）and  (逻辑与,  具有'并且'含义)
# 作用：判断顺序是从左至右，若两边的值都为真，则返回后一个为真的值；若有一个为假，则返回第一个为假的值。
# 核心思想：短路逻辑
# 短路逻辑：在逻辑运算中，运算符的求值过程会根据运算结果提前终止，不再继续计算后面的部分。
# ① and两边链接的是表达式
print(2 > 3 and 4 > 1)
# 2>3 and 4>1
# False and True
# 计算的结果是：False
# 左边为假的值是作为整个表达式的结果

print((2 + 10) <= 23 and 2 > 0)
# (2 + 10) <= 23 and 2 > 0
# 12<=23 and 2>0
# True and True
# True
# 如果左边为真就不符合短路逻辑，继续判断右边的值。
# 如果两边的结果都为真，整个表达式的结果：右边为真的值。

print(10 - 1 and 8 + 6)
# 10 - 1 and 8 + 6
# 9 and 14
# 14
# 不管是9还是14布尔值为真
# 我们是通过布尔值比较真假，结果不一定是布尔值

# ② and两边链接的可能是数值类型、变量、表达式等
print(1.6 and 4 > 7)
# False

name = "张三"
print(34 < 67 and name)
# '张三'

print(name and 145)
# 145

print(1.2 + 9.36 and "")
# ''

print(10 - 10.0 and True)
# 符合短路逻辑的
# 0.0

# ③ and还可以链接多个表达式
print(10 > 3 and 10 and 0 and 4 == 4 and 3 != 3)
# 10 > 3 and 10 and 0 and 4 == 4 and 3 != 3
# 0

# 如果有遇到布尔值为假的值，那么整个and表达式结果就是这个值
# 如果没有遇到布尔值为假的，整个表达式的结果就是最后一个布尔值为真的值


# 3)  or  (逻辑或)
# 作用：判断的顺序是从左至右,返回第一个为真的值，如果两边的值的布尔值都为假，则返回最后一个布尔值为假的值。
# 核心思想：短路逻辑
# ① or两边链接的是表达式
print(2 > 1 or 78 + 1 < 12)
# 2 > 1 or 78 + 1 < 12
# True or False
# True
# 如果一开始，左边的结果为真，那么就返回左边的值（整个表达式的结果）。
# 符合短路逻辑

print(78 + 1 < 12 or 2 > 1)
# 不符合短路逻辑
# False or True
# True

# and:如果左边为假，符合短路逻辑，整个表达式的结果就是为假的这个值
# or :如果左边为真，符合短路逻辑，整个表达式的结果就是为真的这个值
print(2 < -12 or 78 + 1 < 12)
# False

print(0 or 9 + 1)
# 10

# ② or 两边链接的可能是数值、变量、表达式等
print(1 or 2 > 4)
# 1

age = 19
print(age or 1 > 0)
# 19

age = 0
print(3.5 > 12 or age)
# 0

print(age - 21.0 or 39)
# -21.0 or 39
# -21.0

print(2 < 3 or 1)
# 2 < 3--> True

# ③ or 链接多个表达式
print(67 % 5 > 3 or "string" == 0 or 41 or (2 ** 3 // 2) > 66)
# 41 or (2 ** 3 // 2) > 66
# 41

# 找第一个为真的值
# 如果都为假，整个表达式的结果就是最后一个为假的值。


# 练一练
print(12 < 1 and 0 or 23 > 1)
# 优先级：and > or
# 12 < 1 and 0 or 23 > 1
# False or 23>1
# 23>1 -->True

# and 只要一个不成立，那结果就是不成立，or 也是偷懒原则，只要有一个成立，那结果就是成立。

print(20 or 10 > 12 and 20 < 210 or 52 < 53)
# 20 or False or 52 < 53
# 20

print(84 != 73 and not 22 > 22 or 31 == 27 and '张三' == '李四' or 18 > 20)
# True or False or 18 > 20
# True

print(0 or 12 < 13 and 12)
# 0 or 12
# 12

print(84 != 73 and (not 22 > 22 or 31 == 27) and '张三' == '李四' or 18 > 20)
# False or 18 > 20
# False


