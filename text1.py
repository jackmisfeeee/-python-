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
# Sum = 0
# for i in range(1, 6):
#     Sum += i
#     print(Sum)
# print(Sum)
# for row in range(1, 3):
#     for col in range(1, 4):
#         print(f"a{row}{col}\t\t", end='')
#         col += 1
#     row += 1
#     print("\n\n")
# st = '我今天早上没课a~hh好'
# a = st.encode('utf-8')
# print(a, type(a))
# print(a)
# b = a.decode('gbk')
# # st1 = "中午去食堂吃饭666"
# b = a.decode('utf-8')
# print(b, type(b))
# name = "liuyuan"
# print(name[3:10:2])  # 起始：结束：步长
# print(name[:])
# print(name[3:7])  # 起始-结束距离代表切取个数，包前不包后，(a,b]  #7-3=4
# print(name.find('liu'), name[0:3])
# print(name.lower())
# print(name.count('u'), name.index('yuan'), name.endswith('yuan'))
# print(name.replace('liu', 'yuan'))
# print(name.title())
# print(name.split('y'))
# print(name.capitalize())
# st = 'peace and love'
# print(st.title())
# print(st.upper())
# st = st.upper()
# print(st)
# print(st.lower())
# print(st.strip())
# name = 'liuyuan'.lower()
# print(name.endswith('liu'))
# print(name.startswith('liu'))
# print(name.endswith('yuan'))
# print(name.startswith('u', 2, 5))
# print(name.endswith('n', 2, 6))
# print(name.endswith('n', 2, 7))
# print(name.islower())
# print(name.isupper())
# print(name.casefold())
# x = 1
# print(f'{x+1=}')   # Python 3.8
# st2 = '123454'
# print(st2.isdigit())
# st = 'adgddfasdadadwwsds2323wdasdwadad'
# print(st.isalpha())
# print(st.isdigit())
# print(st.islower())
# print(st.isupper())
# print(st.isspace())
# print(st.istitle())
# print(st.isspace())
# print(st.isdecimal())
# print(st.isnumeric())
# print(st.isalpha())
# print(st.isalnum())
# s1 = '~'
# s2 = '_'
# seq = ('abc', 'def', 'ghi', 'hhh')
# str = 'dasdw1234'
# print(s1.join(seq))
# print(s2.join(seq))
# print(len(seq))
# print(len(str))
# print(min('a', 'b'))
# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(seq))
# print(seq[0])
# print(seq[-1])
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# lsit2 = range(len(list1))
# print(lsit2)
# print(type(lsit2))
# # print(list1)
# # print(type(list1))
# import types
#
# # 获取 types 模块中定义的所有属性和方法
# all_types = dir(types)
#
# # 打印 types 模块中定义的所有类型
# for t in all_types:
#     print(t)
# while 1 > 0:
#     print("Hello, world!")
# print(9 ** 0.5)
# multiples = [i for i in range(30) if i % 3 == 0]
# print(multiples)
# # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
# names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# new_names = [name.upper() for name in names if len(name) > 3]
# print(new_names)
# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。
'''
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''

# 计算 30 以内可以被 3 整除的整数
# a = [i for i in range(30) if i % 3 == 0]
# print(a)
# print(id('hello'))
# print(id(type('world')))
# # print(r"rrrr\n")
# def sum1(num1, num2):
#     Sum = num1 + num2
#     print("函数内是局部变量", Sum)
#     return Sum
#
#
# s = sum1(3, 5)
# print(s)
# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# globvar = 0
#
#
# def set_globvar_to_one():
#     global globvar  # 使用 global 声明全局变量
#     globvar = 1
#
#
# def print_globvar():
#     print(globvar)  # 没有使用 global
#
#
# set_globvar_to_one()
# print(globvar)  # 输出 1
# print_globvar()  # 输出 1，函数内的 globvar 已经是全局变量
# num = int(input('输入一个四位整数：'))
# ones = num // 1000
# print(f"ones={ones}")
# tens = num // 100 % 10
# print(f"tens={tens}")
# hundreds = num // 10 % 10
# print(f"hundreds={hundreds}")
# thousands = num % 10
# print(f"thousands={thousands}")
# Sum = ones + tens + hundreds + thousands  # 可以用一个求和函数来替换
# print(f"各个位数之和为：{Sum}")
#
# num = (input('输入'))
# print(int(num[-1]))
x = '你简直无敌了'
