# 第一次作业
# 完成的同学可以复制代码发送到192839560@qq.com（备注班级+姓名）
# 祝大家周末愉快！~


# 一、单选题：
# 1、下列表达式的值为True的是（C）。
# A. not(11 and 0 != 2)
# B. 3>2>2
# C. 1 and 2 != 1
# D. 10 < 20 and 10 < 5

# 2、运⾏以下程序，当从键盘上输入10,运行结果是（B）。
# n = input('请输入：')
# print(type(n+1))
# A. <class 'int'>
# B. 出错
# C. <class 'dict'>
# D. <class 'str'>

# 3、下列表达式的运算结果是（ A）。
# a = 100
# b = False
# print(a * b < -1)
# A. False
# B. 1
# C. 0
# D. True

# 4、以下优先级正确的是：（ A）。
# A. 算术运算符 > 比较运算符 > 逻辑运算符
# B. 算术运算符 > 逻辑运算符 > 比较运算符
# C. 比较运算符 > 逻辑运算符 > 算术运算符
# D. 逻辑运算符 > 算术运算符 > 比较运算符

# 5、Python成员运算符"in"用于判断某个值是否为序列中的成员，如果是的话就返回"True"，否则就返回"False"。由此可知，下列表达式中值为"True"的是（A ）。
# A. "hel" in 'hello'
# B. "春"in"野火烧不尽"
# C. 13 in [1,2,3,4]
# D. "海上" in ["上海"，"深圳"，"佛山"，"东莞"]


# 6、下列选项中结果为True的是（A ）。
# A. "张三" != "罗翔"
# B. 'world' == type('hello')
# C. '张三' is '李四'
# D. 'world' is type('hello')


# 二、填空题：
# 1、查看变量中数据的类型的函数名是（ type）。

# 2、a = 10 和 a == 10 区别在于（前者是将10赋值给变量a，后者是判断a是否等于10 ）。

# 3、已知 x = 3 == 6 ,执行结束后，变量x的值为（ 3）。

# 4、已知 x = 3 ，那么执行语句 x += 17之后，x的值为（ 20 ）。

# 5、表达式 3 ** 5 的值为（ 243）,表达式 3 * 4 的值为（ 12 ），表达式 9 ** 0.5 的值为（ 3 ）。

# 6、浮点型变量，将其输出，输出时要求将其保留3位小数，如何书写（ 假设变量名为x,写法为：print(f'{x:.3f}')）。

# 三、代码题：
# 1、 简述print函数中三大参数(*values、sep、end)的作用，并举例体现。
# *values是print函数中的输出值参数可以是一个也可以是多个，如：
print("Hello World!", 123, '小庐老师最漂亮')  # 其中就有三个values分别是字符串Hello World，整型数值123,以及字符串小庐老师最漂亮
# sep参数在print函数中的作用是控制各个值之间的分隔符，默认sep=' ' ，即print函数中的各个值默认以空格分隔，比如：
print("Hello", ' World!')  # 输出的就是Hello World。其实在函数中影藏了sep参数
print("Hello", 'World!', sep=' ')  # 如果将参数sep=' '更改，各个值直接分隔方式也会改变。例如：
print("Hello", 'World!', sep=',')  # 输出为Hello，World！
print("Hello", 'World!', sep='：')  # 输出为Hello：World！
print("Hello", 'World!', sep='---')  # 输出为Hello---World！

# end参数在print函数中的作用是指定函数输出结束时的字符或者字符串，默认end='\n',即print函数默认以换行符结束，执行换行操作，比如：
print("Hello", 'World!')
# 在输出后默认会换到下一行，会在程序结束提示语Process finished with exit code 0之间多一行空白行
# 同样，和sep参数相似，end参数的默认值也能更改，如：
print("Hello", end='')  # 输出Hello后以空字符结尾
print("Hello", end=' ')  # 输出Hello后以空格结尾
print("Hello", end='\t')  # 输出Hello后以制表符结尾
print("Hello", end='，')  # 输出Hello后以，结尾
# eg：
print("Hello", "World", sep='\t', end=' ')
# 输出：Hello    World
# 2、输入两个数字，分别保存给两个变量,将这两个变量进行加减乘除运算 并 分别格式化输出计算结果。
variable1 = int(input("Enter1:"))
variable2 = int(input("Enter1:"))
sum = variable1 + variable2
difference = variable1 - variable2
product = variable1 * variable2
quotient = variable1 / variable2
print("sum=%.2f, difference=%.2f, product=%.2f, quotient=%.2f （结果均保留两位小数）" % (
    sum, difference, product, quotient))
print("sum=%.2f, difference=%2d")
# 3、改写代码，如何让下面的程序不报错，并写出报错原因。
# number = input('输入：')
# print(number > 11 )
# 可改成：
number = int(input('输入整数：'))
print(number > 11)
# 原因是input函数默认接收字符串类型，字符串和整型11在Python中不能进行比较运算
# 并且没有规定输入是什么，比较运算符只能进行同类型比较而且print()中11后面加了空格不规范

# 4、 编写一个程序，在控制中同时输出单引号和双引号。
# 例如控制台效果："Hello" 'world'！
print(""""Hello" 'World!'""")

# 5、 x = 10, 以下表达式运行结果一样吗？
# x = 10
# x = x * 2 + 6
# x *= 2 + 6

# 答：不一样
# x = x * 2 + 6  =>  x = 10 * 2 + 6 = 20 + 6 = 26
# x *= 2 + 6     =>  x = x *（2+6）= 10 * 8 = 80

# 6、 口算快速计算下列变量结果
a = 2
b = 4
c = 3
d = 6
s1 = a + b + c + d  # 15

s2 = a + b * c // 3 + d  # 12

s3 = a / b + c ** 2 / d  # 2.0

s4 = a + b * c + a / b % 3  # 14.5

s5 = a <= b >= c  # Ture

s6 = -a + b == c > d  # False

s7 = b + c == 6 + d >= 13  # False

# 7、 判断下列逻辑语句的结果：
# 1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# Ture
# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# False
# 3) 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8
# 4) 0 or 2 and 3 and 4 or 6 and 0 or 3
# 4
# 5) 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# 2

# 8、测验驾驶员是否酒驾，血液酒精含量小于20不构成酒驾，大于20则再判断是否小于80，如果是则判定酒驾，大于等于80则判定醉驾。
for i in range(1, 11):  # 循环10次测试代码
    AlcoholContent = float(input('酒精含量：'))  # 在控制台输入数值作为检测值
    if AlcoholContent > 0:
        if 20 > AlcoholContent:  # 酒精含量在(0,20),判定为没有酒驾
            print('不构成酒驾')
        elif 20 <= AlcoholContent < 80:  # 酒精含量在[20,80),判定为酒驾
            print('构成酒驾')
        else:  # 酒精含量>=80,判定喝麻了，醉驾
            print('构成醉驾')
    else:
        print('检测错误')

# 9、编写代码，输入一个成绩，通过判断输出成绩等级：
# 分数为100分，为S等级；
# 分数为90分至99分为A等级；
# 分数为80-89分为B等级；
# 分数为60-79为C等级；
# 分数低于60为D等级；
# 其他则成绩无效。
# 示例：分数为80分 输出结果B等级。
for i in range(1, 11):  # 循环10次测试代码
    score = float(input('输入成绩:'))
    if 0 < score <= 100:  # 输入成绩在(0,100],进入判断
        if 100 == score:  # 如果成绩=100，成绩等级为S
            print('S')
        elif 90 <= score <= 99:  # 如果成绩在[90,99]，成绩等级为A
            print('A')
        elif 80 <= score <= 89:  # 如果成绩在[80,89]，成绩等级B
            print('B')
        elif 60 <= score <= 79:  # 如果成绩在[60,79]，成绩等级C
            print('C')
        else:  # 如果成绩在(0,60)，成绩等级D
            print('D')
    else:
        print("成绩无效")  # 如果成绩不在(0,100]范围，成绩无效

# 10、 输入一个四位整数,计算各个位数相加的和。
# 例如：n=1234,各个位数和为10。
num = int(input('输入一个四位整数：'))
ones = num // 1000
print(f"ones={ones}")
tens = num // 100 % 10
print(f"tens={tens}")
hundreds = num // 10 % 10
print(f"hundreds={hundreds}")
thousands = num % 10
print(f"thousands={thousands}")
sum = ones + tens + hundreds + thousands  # 可以用一个求和函数来替换
print(f"各个位数之和为：{sum}")

