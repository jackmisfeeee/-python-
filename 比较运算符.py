# 作用：用于比较两个值的运算符，返回一个布尔值（True或False），表示比较的结果是否成立。

# 1、==
# ==是比较运算符，=是赋值运算符，不要混淆。
# (x、y代指某一个操作数、表达式)
# 作用：比较x和y的值是否相等，如果相等返回布尔值True，不相等返回的False。
print(2 == 3)  # False
print(6 == 6)  # True
print(0.0 == 0)  # True 不会比较类型
print(2 + 5 == 6 + 1)  # True 优先级：算术运算符 > 比较运算符

# 2、！=
# 作用：比较x和y的值是否不相等，如果不相等返回布尔值True，否则相等返回False
print(2 != 3)  # True
print(2 != 2)  # False

# 3、> >=
# > 比较x值是否大于y的值，如果大于返回布尔值True，否则返回False。
print(3 > 2)  # True
print(23.0 > 13)  # True
print(True > False)  # True
print(190.6 < 3 * True)  # False

# >= 比较x值是否大于或者等于y的值，只要是满足其中一个，返回布尔值True，都不满足则返回False。
print(23 >= 6)  # True
print(23 >= 23)  # True
print(13 >= 23)  # False
age = 19 / 2  # 9.5
print(age >= 10)  # False

# 4、< <=
# < 比较x值是否小于y的值，如果小于返回布尔值True，否则返回False。
print(4 < 6)  # True

# <= 比较x值是否小于或者等于y的值，只要是满足其中一个，返回布尔值True，都不满足则返回False。
print(4 <= 6)  # True
print(6 <= 6)  # True

# 注意1：在比大小(> >= < <=)的时候，两边的操作数或表达式必须为同类型，否则程序就会报错。
# print(1 < '2')
# TypeError: '<' not supported between instances of 'int' and 'str'

print(1 < 1.5)  # 都属于数值类型

# 注意2：== 和！= 运算符两边的值可以是不同类型数据也可以是相同类型数据。
print(1 == 1)
print(1 == '1')
# True
# False

# 5、字符串可以和字符串比较大小？可以
print("python" >= "pycharm")

# 字符串怎么去比大小？
# 字符和字符比较是根据ASCII编码表对应的数字进行比较。
# 关于ASCII码，它是一种字符编码方式,用于将字符转化为数字,方便计算机识别和处理。
# 比如：0对应的ASCII码值是48, 1对应的是49，所以1肯定是大于0的。
# 大写A~Z的ASCII码值是65 - 90，小写a~z的ASCII码值对应的是97 - 122。
print("Balance" > "average")  # False

# 长度不同的情况：
# 如果两个字符串的前缀完全相同，但是它们的长度不同，较短的字符串默认是较小的。
str1 = "apple"
str2 = "app"
print(str1 > str2)  # True

# 注意：如果是数字字符串比大小，可能会有一些bug
print(9 > 1)
print('9' > '1')

print('9' < '102')  # False

# ord()函数
# 作用：将一个字符转换成其对应的 Unicode 编码值。
# 语法：ord(character)
# character参数是一个用引号包围起来的单个字符
print(ord('A'))
print(ord('a'))
# 65
# 97

print(ord('你'))  # 20320

#  chr()函数
# 作用：将整数 Unicode 编码转换为对应的字符。
# 语法：chr(i)
# i参数是一个整数，表示码值。
print(chr(48))  # 0

# 比较运算符作用：在编程中经常用于条件判断和逻辑运算，帮助我们控制程序的执行流程。


