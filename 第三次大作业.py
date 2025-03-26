# 第三次作业
# 完成后复制发送邮箱到192839560@qq.com(备注姓名+班级)
# 祝大家周末愉快！！

# 一、单选题：
# 1、for循环用于遍历可迭代对象，下列选项中完全遍历了列表里的元素的是：【 a】
# - B. for i in range(my_list):
#         print(i)

# - C. for i in range(len(my_list)):
#         print(i)

# - A. for item in my_list:
#         print(item)

# - D. for i in range(len(my_list)-1,0,-1):
#         print(my_list[i])


# 2、推算下列代码中a的输出结果：【D 】
a = []
for i in range(2, 10):
    count = 0
    for x in range(2, i - 1):
        if i % x == 0:
            count += 1
            if count == 1:
                a.append(i)
# - A. [2, 4, 6, 8]
# - B. [4, 6, 8, 9, 10]
# - C. [2, 3, 5, 7, 9]
# - D. [4, 6, 8, 9]


# 二、多选题：
# 1、以下哪些是集合的特性：【 ABc 】
# - A. 无序性
# - B. 唯一性
# - C. 数据必须为不可变类型
# - D. 可重复

# 2、以下哪些是字典的方法：【 BCD 】
# - A. 字典名.key()
# - B. 字典名.values()
# - C. 字典名.items()
# - D. 字典名.get()

# 3、len函数可以计算哪些数据的长度：【 ABD 】
# - A. 字典
# - B. 集合
# - C. 整型
# - D. 字符串

# 4、 Python中的数据结构可分为可变类型与不可变类型,下面属于不可变类型的是：【 AC 】
# - A、元祖
# - B、列表
# - C、字典中的键
# - D、集合

# 5、以下说法正确的是：【 BD 】
# - A. 函数的定义阶段会执行代码
# - B. 函数必须先定义后调用
# - C. 函数名可以随便设定,不用遵守标识符规定
# - D. 函数定义关键字是def


# 三、代码题
# 1、定义列表存放5个学生的成绩（自定义），输出一个字典里包含：成绩之和、平均成绩、最小成绩、最大成绩。
# 比如：{'成绩和':xxx,'平均成绩':xxx,...}
# 方法1 自己写
# 成绩列表：
students_grade = [100, 88, 76, 54, 31]
# 成绩和：
s = 0
for i in students_grade:
    s += i
# 平均值
average = s / len(students_grade)


# 最大最小成绩
def my_max(ob):
    result1 = ob[0]
    for number in ob:
        if number > result1:
            result1 = number
    return result1


def my_min(ob):
    result2 = ob[0]
    for number in ob:
        if number < result2:
            result2 = number
    return result2


max1 = my_max(students_grade)
min1 = my_min(students_grade)
end_result = {'成绩之和': s, '平均成绩': average, '最大成绩': max1, '最小成绩': min1}
print(end_result)

# 方法2 用内置函数写
students_grade = [100, 88, 76, 54, 31]
# 和
s1 = sum(students_grade)
# 平均
ave = s1 / len(students_grade)
# 最大
max2 = max(students_grade)
# 最小
min2 = min(students_grade)
result_dict = {'成绩之和': s1, '平均成绩': ave, '最大成绩': max2, '最小成绩': min2}
print(result_dict)


# 2、编写函数，计算传入一个字符串中的数字、字母、空格以及其他的个数，返回一个字典{'数字个数':xx,'字母个数':xx...}。
def count_char_type(t):
    # 初始化数字，字母，空格，和其他类型计数器为0
    digit_count = 0
    letter_count = 0
    space_count = 0
    other_count = 0
    for char in t:
        if char.isdigit():
            digit_count += 1

        elif char.isalpha():
            letter_count += 1

        elif char.isspace():
            space_count += 1

        else:
            other_count += 1

    res = {'数字': digit_count, '字母': letter_count, '空格': space_count, '其他类型': other_count}
    return res


# 测试 text
print(count_char_type('12345abcde     False  测试[1,2](1,2){1:}'))
# {'数字': 10, '字母': 12, '空格': 7, '其他类型': 9}

# 3、有如下值[11, 22, 33, 44, 55, 66, 77, 88, 99, 90], 将所有大于或等于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
result = \
    {
        'key1': [i for i in lst if i >= 66],
        'key2': [i for i in lst if i < 66]
    }
print(result)


# 4、交换字典的key和value，产生新字典。
# 比如：{'张三' :23 ,'李四' :33 ,'王五' :44}
# 交互后：{23: '张三', 33: '李四', 44: '王五'}
# 定义一个交换函数
def swap_dict(dictionary):
    return {value: key for key, value in dictionary.items()}


dict1 = {'张三': 23, '李四': 33, '王五': 44}
dict2 = swap_dict(dict1)
print(dict2)

# 5、用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)。
python = ('stu1', 'stu2', 'stu6', 'stu7', 'stu9', 'stu10', 'stu11')
c = ('stu1', 'stu3', 'stu6', 'stu8', 'stu9')
java = ('stu1', 'stu2', 'stu4', 'stu5', 'stu8', 'stu9')
# 5.1 求选课学生总共有多少人;
# 利用集合的唯一性 将多个元组的内容进行整合，得到唯一不重复的元素
s1 = set(python)
s2 = set(java)
s3 = set(c)
sn = s1 | s2 | s3
print(sn)
# 人数
print(f"选课的总人数为:{len(sn)}")

# 5.2 求只选了第一个学科的人的数量和对应的名字;

only_python = s1 - (s2 | s3)
print(f"只选了 Python 课程的学生数量为: {len(only_python)}")
print("只选了 Python 课程的学生集合：", only_python)

# 5.3 求只选了一门学科的学生的数量和对应的名字;

# 只选了s1（python）的学生为
s_only_python = s1 - (s2 | s3)
# 只选了s2(c)的学生为
s_only_c = s2 - (s1 | s3)
# 只选了s3(java)的学生为
s_only_java = s3 - (s1 | s3)
total = s_only_java | s_only_python | s_only_c
print(f"只选了一门学科的学生数量为：{len(total)}")
print(f"只选了一门学科的学生集合为：{total}")

# 5.4 求选了三门学生的学生的数量和对应的名字。

all_select = s1 & s2 & s3
print(f"三门学科都选的学生有: {len(all_select)}人")
print(f"三门学科都选了的学生集合：{all_select}")

# 6、编写程序：提示用户输入一个1-15之间的正整数,然后显示一个数字金字塔。
# 输入：7, 运行如下所示：

#                   1
#                2  1  2
#             3  2  1  2  3
#          4  3  2  1  2  3  4
#       5  4  3  2  1  2  3  4  5
#    6  5  4  3  2  1  2  3  4  5  6
# 7  6  5  4  3  2  1  2  3  4  5  6  7

try:
    num = int(input("请输入一个 1 - 15 之间的正整数: "))
    if 1 <= num <= 15:
        for i in range(1, num + 1):
            # 打印空格
            print(" " * (num - i) * 3, end="")
            # 打印递减部分
            for j in range(i, 0, -1):
                print(f"{j:3d}", end="")
            # 打印递增部分
            for j in range(2, i + 1):
                print(f"{j:3d}", end="")
            print()
    else:
        print("输入的数字不在 1 - 15 范围内，请重新输入。")
except ValueError:
    print("输入无效，请输入一个有效的整数。")
