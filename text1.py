# k = """哈哈哈"""
# print(k)
# print('西瓜是'+'三块'+'一斤')
# print(r 'abd\aa\\a\n')
# r -- 原生字符 效果和\\一样 使输出中的转义字符无效化
# name = "zhang san"
# num = 3
# print(name*num)
# a = ''''''
# print(True+False1)
# age = 12
# if isinstance(age, str):
#     print("字符型")
# if isinstance(age, int):
#     print("整型")
# if isinstance(age, float):
#     print("浮点型")
# # -----------------------------------------------------
# day = 2
# time = 7
# if day > 1 and time >= 7:
#     print("早起")
# else:
#     print("睡大觉")
# while 1:
#     print(10*100)
"""
Created on
"""
# a = 123
# for i in "bingbing":
#     print(i)
# for i in "123456":
#     print(i)
# while循环嵌套
# row = 1
# while row < 3:
#     column = 1
#     while column <= 4:
#         print(f"第{row}行第{column}列")
#         column += 1
#     print('\n')
#     row += 1
# print("over process")
# s = 0
# for i in range(1, 101, 1):
#     s += i
# print(s)
# 0、None、空字符串、空列表、空元组、空字典、空集合等布尔值为False，其他类型数据的布尔值为True。
# False的本质是0，True的本质是1。

# number = input('输入：')
# print(number > "hhh")
# x = 10
# # x = 10
# # x = x * 2 + 6
# x *= 2 + 6
# print(x)

# a = 2
# b = 4
# c = 3
# d = 6
# s1 = a + b + c + d  # 15
# print(s1)
# s2 = a + b * c // 3 + d  # 12
# print(s2)
# s3 = a / b + c ** 2 / d  # 2.0
# print(s3)
#
# s4 = a + b * c + a / b % 3  # 14.5
# print(s4)
#
# s5 = a <= b >= c  # Ture
# print(s5)
#
# s6 = -a + b == c > d  # False
# print(s6)
#
# s7 = b + c == 6 + d >= 13  # False
# print(s7)
# 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# Ture
# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# False
# 3) 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8
# 4) 0 or 2 and 3 and 4 or 6 and 0 or 3
# 4
# 5) 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# # 2
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
# for i in range(1, 11):   # 循环10次测试代码
#     AlcoholContent = float(input('酒精含量：'))  # 在控制台输入数值作为检测值
#     if AlcoholContent > 0:
#         if 20 > AlcoholContent:  # 酒精含量在(0,20),判定为没有酒驾
#             print('不构成酒驾')
#         elif 20 <= AlcoholContent < 80:  # 酒精含量在[20,80),判定为酒驾
#             print('构成酒驾')
#         else:  # 酒精含量>=80,判定喝麻了，醉驾
#             print('构成醉驾')
#     else:
#         print('检测错误')
# for i in range(1, 11):  # 循环10次测试代码
#     score = float(input('输入成绩:'))
#     if 0 < score <= 100:    # 输入成绩在(0,100],进入判断
#         if 100 == score:    # 如果成绩=100，成绩等级为S
#             print('S')
#         elif 90 <= score <= 99:     # 如果成绩在[90,99]，成绩等级为A
#             print('A')
#         elif 80 <= score <= 89:     # 如果成绩在[80,89]，成绩等级B
#             print('B')
#         elif 60 <= score <= 79:     # 如果成绩在[60,79]，成绩等级C
#             print('C')
#         else:                       # 如果成绩在(0,60)，成绩等级D
#             print('D')
#     else:
#         print("成绩无效")           # 如果成绩不在(0,100]范围，成绩无效
# 10、 输入一个四位整数,计算各个位数相加的和。
# 例如：n=1234,各个位数和为10。
# num = int(input('输入一个四位整数：'))
# ones = num // 1000
# print(f"ones={ones}")
# tens = num // 100 % 10
# print(f"tens={tens}")
# hundreds = num // 10 % 10
# print(f"hundreds={hundreds}")
# thousands = num % 10
# print(f"thousands={thousands}")
# sum = ones + tens + hundreds + thousands
# print(f"各个位数之和为：{sum}")
# row = 1
#
# while row <= 4:
#     column = 1
#     while column <= 4:
#         print(f"第{row}行第{column}列", end="\t")
#         column += 1
#     row += 1
#     print("\n")
Sum = 0
for i in range(1, 6):
    Sum += i
    # print(Sum)
print(Sum)
for row in range(1, 3):
    for col in range(1, 4):
        print(f"a{row}{col}\t\t", end='')
        col += 1
    row += 1
    print("\n\n")
