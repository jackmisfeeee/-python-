# 第二次作业
# 写完的同学可以复制代码，发送到邮箱192839560@qq.com（备注：姓名+班级）
# 祝大家周末愉快！


# 一、单选题
# 1、关于python循环，以下选项中描述错误的是：【C 】
# - A. python通过for、while等关键字来提供遍历循环和无限循环结构。
# - B. break/continue在嵌套循环中，只对最近的一层循环起作用。
# - C. continue可以用于单独的if判断中。
# - D. for循环可以用于遍历取值。


# 2、想通过for循环来打印出1-10之间的数(包括10),下列代码选项正确的是：【 C】
# - A、for i in range(10):
#          print(i)

# - B、for i in range(11):
#          print(i)

# - C、for i in range(1,11):
#          print(i)

# - D、for i in range(1,10):
#          print(i)


# 3、仔细阅读下列代码,选出你认为正确的选项：【B 】
# s=0
# for i in range(0,10,2):
#     s+=i
# print(s)
# - A、该代码求的是1-10之间所有数的和,结果是45。
# - B、该代码求的是0,2,4,6,8这五个数的和,结果是20。
# - C、该代码求的是1,3,5,7,9这四个数的和,结果是25。
# - D、该代码求的是2,4,6,8,10这五个数的和,结果是30。


# 二、多选题
# 5、以下哪些类型可以被for循环遍历：【BC 】
# - A. 123
# - B. "abc"
# - C. '58458486'
# - D. True


# 6、以下关于循环说法正确的是：【ABD 】
# - A. break退出当前循环。
# - B. for循环能够对可迭代对象进行遍历。
# - C. break和continue必须成对出现。
# - D. break和continue在循环中一般结合if语句使用。


# 7、以下哪些选项的代码不会陷入死循环:【 ACD】  # 其中c会报错 因为n+=1缩进不符合规范

# - A.
# n = 0
# while True:
#     if n == 0:
#         break
#     print(n)

# - B.
# n = 1
# while True:
#     print(n)
# n+=1

# - C.
# n = 1
# while True:
#     print(n)
#       n += 1

# - D.
# for i in range(100):
#     print(i)


# 三、代码题
# 1、Fizz Buzz 经典问题 (提示：这是一道题目，不可拆开来写！)
# 使用for或while循环1-100
# 如果这个数被 3 整除，输出'Fizz'。
# 如果这个数被 5 整除，输出'Buzz'。
# 如果这个数能同时被 3 和 5 整除，输出'FizzBuzz'。
# 如果这个数既不能被 3 也不能被 5 整除，输出这个数字。

# 方法1，使用顺序循环分支基础结构依次检索
# 初始化计数器为1
c = 1
# 控制循环100次
while c < 101:
    # 注意 必须先判定是否同时被3、5整除，才能输出FizzBuzz
    if c % 3 == 0 and c % 5 == 0:
        print('FizzBuzz')
    elif c % 3 == 0:
        print('Fizz')
    elif c % 5 == 0:
        print('Buzz')
    else:
        print(c)
    c += 1

# 方法2，使用一个数据容器来依次判定是否符合条件
# 我发现这种创建列表来控制可以写成一个函数来反复套用的感觉，但是我还没学函数
# 创建一个1-100的列表
list1 = []
t = 1
while t < 101:
    list1.append(t)
    t += 1
# 开始检索列表元素符合条件并依次输出
for i in range(100):
    if list1[i] % 3 == 0 and list1[i] % 5 == 0:
        print('FizzBuzz')
    elif list1[i] % 3 == 0:
        print('Fizz')
    elif list1[i] % 5 == 0:
        print('buzz')
    else:
        print(list1[i])
# 程序结束得到结果

# 2、字符串练习题
# 2.1 判断输入的字符串是否是.py结束；

# 1.原始人方法：
# 创建一个变量接收字符串
s = input('请输入：')
# 切片最后三个字符
split1 = s[-3::]
# 判断
if split1 == '.py':
    print('yes')
else:
    print('no')

# 2.使用字符串判断方法
s = input('请输入：')
if s.endswith('.py'):
    print('yes')
else:
    print('no')

# 2.2 原生字符串如何表示？
print(r'')
# 2.3 "this is a book",请将字符串里的book替换成apple；
s = "this is a book"
s = s.replace('book', 'apple')
# 2.4 string = "Python is good", 请将字符串里的Python替换成python,并输出替换后的结果。
str_change = "Python is good".replace('Python', 'python')
print(str_change)
# or
str_change = "Python is good".lower()
print(str_change)
# or
print("Python is good".lower())
# 3、 口述回答下面代码输出的结果:
string = "Python is good"

# string[1:20]  # y到d全部内容
# string[20]    # 索引下标超出字符串下标范围 max=13
# string[3:-4]  # h到g前面的空格全部内容 hon is空格

# 4、一张纸的厚度大约是0.08mm，计算对折多少次之后能达到或超过珠穆朗玛峰的高度（8848.13米）
"""
思路：
1、设定条件纸的厚度初始值为0.08，定义对折次数变量为0；
1. 使用循环，当循环条件变量大于8848.13则退出循环；
2. 每对折一次纸的厚度增加一倍；记录对折次数变量+1
注意单位换算！
"""
# 简单
# 初始化厚度为0.08mm
Thickness = 0.08
# 初始化计数器
count = 0
# 初始化珠峰高度转换成毫米（mm)
the_height_of_Mount_Everest = 8848.13 * 1000
while Thickness < the_height_of_Mount_Everest:
    Thickness *= 2
    count += 1
print(f"对折{count}次后能达到或超过珠穆朗玛峰的高度（8848.13米）")
# 有趣的是这里的厚度映射的函数为y=0.08*2**x 当x=26时 y = 5368709.12 而当x=27时 y=10737418.24 就达到一万多米了 指数型函数的压迫感~

# 5、 循环提示用户输入，并将输入内容追加到列表中（如果用户输入N或n则停止循环），输入结束则打印列表。
# 如果用户输入的信息已经存在，则提示用户所输内容已存在，不要重复添加。

# 定义一个空列表用来存放输入内容
lis = []
# 初始化传递变量
# t = 0
while True:
    # 提示用户输入内容
    t = input('请输入内容（输入n或者N停止）：')
    # 如果输入的内容是n或者N 退出循环
    if t.lower() == 'n':
        break
    # 如果输入的值已经在列表中，提示用户所输内容已存在，不要重复添加
    if t in lis:
        print('输入内容已经存在，不要重复添加')
    else:
        # 将输入的值加进列表
        lis.append(t)
# 输出列表
print(lis)

# 6、输入两个整数，分别赋值给m和n，计算m到n之间的数字和(包含m和n).
# 考虑如果出现m大于n的情况怎么办？

# 初始化数字和为0
num_sum = 0
# 输入两个整数，分别以整型赋值给m和n
m = int(input('请输入第一个整数:'))
n = int(input('请输入第二个整数:'))
# 先将m ，n 相加放入数字和
num_sum += m + n
# 将mn之间输入赋值给数字和
# 如果m的值大于n的值进入语句块
if m > n:
    # 如果mn间隔大于1中间才有非零整数 否则之间的整数有且只有0
    if m - n > 1:
        # 当n 小于 m时执行下面语句
        while n < m - 1:
            # n的值加一
            n += 1
            # 此时的n后的那个整数就是mn之间最小的那个整数 赋值给number_sum
            num_sum += n
    else:
        num_sum += 0
# 如果n 大于 m 执行相似操作
elif n > m:
    if n - m > 1:
        while m < n - 1:
            m += 1
            num_sum += m
    else:
        num_sum += 0
# 如果m 和n 中的值相等
else:
    num_sum += 0
print(f'{m}到{n}之间的数字和（包含{m}和{n}）为：{num_sum}')

# 豆包给出的代码 太简洁了666~~
# 提示用户输入两个整数
m = int(input("请输入第一个整数 m: "))
n = int(input("请输入第二个整数 n: "))

# 判断 m 和 n 的大小关系
if m > n:
    # 如果 m 大于 n，交换 m 和 n 的值
    m, n = n, m

# 计算 m 到 n 之间的数字和
total = sum(range(m, n + 1))

# 打印结果
print(f"{m} 到 {n} 之间的数字和（包含 {m} 和 {n}）为: {total}")
