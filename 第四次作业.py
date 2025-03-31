# 第四次作业
# 写完的同学可以复制代码，发送到邮箱192839560qq.com（备注：姓名+班级）
# 祝大家有个美好愉快的周末！

# 一、单选题
# 1、关于函数,下列说法中不正确的是：( D )
# - A. 函数就是一段封装好的代码
# - B. 函数能够实现代码的重用
# - C. 函数可以有多个值返回
# - D. 函数的位置参数可以随意传递，不用按照顺序传值

# 2、以下关于Python函数的描述中，正确的是：( C )
# A. 函数eval()可以用于数值表达式求值，例如eval(2*3+1)
# B. Python中def和return是函数必须使用的保留字
# C. Python函数定义中没有对参数指定类型，这说明参数在函数中可以当作任意类型使用，这是Python语言灵活性的体现
# D. 一个函数中只允许有一条return语句

# 3、使用形式参数的名字来确定输入的参数值,指的是什么参数：( D )
# A. 位置参数
# B. 默认参数
# C. 形式参数
# D. 关键字参数

# 4、下述操作不改变对象本身的是：( B )
# A、list.insert(2,'A')
# B、'abc'.replace('a','111')
# C、del dic['key1']
# D、s.add('A')


# 二、多选题
# 1、关于函数,以下选项中描述正确的是：( AC )
# A.函数是一段具有特定功能的可重用的语句组
# B.函数能完成特定的功能，对函数的使用不需要了解函数内部实现原理，只要了解函数的输入输出方式即可
# C.使用函数的主要目的是降低编程的难度和代码复用
# D.Python使用del保留字定义一个函数

# 2、使用已存在的字典作为函数的可变参数,需要: ( C )
# A. 直接使用字典名称作为参数
# B. 在字典名称前加'*'
# C. 在字典名称前加'**'
# D. 在字典内每个元素前加'**'

# 3、以下关于global关键字的作用正确的是：( AB )
# A. 声明一个变量为全局变量
# B. 在函数内部对全局变量进行修改
# C. 没什么作用
# D. 和nonlocal作用完全一样

# 4、在python中，函数参数支持的类型有：( BCD )
# A. 必备参数
# B. 默认参数
# C. 关键字参数
# D. 可变参数


# 三、代码题
# 1、编写一个函数，提示用户小明输入密码，如果小明输入长度超过8位数且密码不是'123456' 则抛出异常，否则返回"密码输入成功！"。为了防止程序终止，请对异常进行处理。
PASSWORD = "123456"
try:
    password = input("请输入密码：")
    if len(password) < 8:
        if password == PASSWORD:
            print("密码输入成功！")
        else:
            raise Exception("密码输入错误！")
    else:
        raise Exception("密码长度超过8位数！")
except Exception as e:
    print(e)

# 2、 编写一个函数，传入两个整数start和end,然后输出这两个整数之间的一个随机数。
# 要求考虑用户传入不是整数的情况，以及start>end的情况，主动去引发异常。
# 并根据实际情况进行适当提示或输出。
try:
    start = int(input("请输入开始整数："))
    end = int(input("请输入结束整数："))
    if start > end:
        raise Exception("开始整数必须小于结束整数！")
    else:
        import random

        num = random.randint(start, end)
        print("随机数为：", num)
except ValueError as e:
    print('输入的必须是整数！')

# 3、写一个函数，实现猜拳游戏。
"""
游戏角色
    玩家 出拳 石头剪刀布 输入input
    电脑 出拳 石头剪刀布 随机出

逻辑判断谁赢谁输
    三个情况
        平局：玩家 == 电脑
        玩家赢：w石头d剪刀  w剪刀d布  w布电脑石头
        电脑赢：...
"""

import random


def rock_paper_scissors():
    choices = ["石头", "剪刀", "布"]
    while True:
        player_choice = input("请出拳（石头/剪刀/布），输入其他内容退出游戏：")
        if player_choice not in choices:
            print("游戏结束。")
            break
        computer_choice = random.choice(choices)
        print(f"你出了 {player_choice}，电脑出了 {computer_choice}。")
        if player_choice == computer_choice:
            print("平局！")
        elif (
                (player_choice == "石头" and computer_choice == "剪刀")
                or (player_choice == "剪刀" and computer_choice == "布")
                or (player_choice == "布" and computer_choice == "石头")
        ):
            print("你赢了！")
        else:
            print("电脑赢了！")


if __name__ == "__main__":
    rock_paper_scissors()

# 4、不运行程序，说出两个print输出的结果分别是什么？
num = 88


def external():
    num = 11

    def inside():
        nonlocal num
        num = 20

    inside()
    print(num + num + num)  # 结果是多少? 60


external()
print(num + num + num)  # 结果是多少? 88+88+88=264


# 5、创建一个完整的Dog类
# 5.1 Dog类有名字、年龄等属性（实例属性）；
# 5.2 定义叫声barking方法，输出动物的叫声；
# 5.3 定义睡觉sleep方法，输出xxx睡觉了；
# 5.4 创建3个动物实例，分别调用实例的叫声方法和睡觉方法。
class Dog:
    def __init__(self, name, age, gender, address, hobby):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.address = address
        self.hobby = hobby

    def barking(self):
        print(f"{self.name} 叫了一声：汪...")

    def sleeping(self):
        print(f"{self.name} 睡觉了...")


# 创建3个动物实例
dog1 = Dog("旺财", 3, "公", "北京", "睡觉")
dog2 = Dog("小黑", 5, "母", "上海", "看电影")
dog3 = Dog("小白", 2, "公", "广州", "拆家")
# 调用实例的叫声方法和睡觉方法
dog1.barking()
dog1.sleeping()
dog2.barking()
dog2.sleeping()
dog3.barking()
dog3.sleeping()
import math


class Circle:

    def __init__(self, r):
        if isinstance(r, (int, float)) and r > 0:
            self.r = r
        else:
            raise ValueError("半径必须是一个正的数字")

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


if __name__ == "__main__":
    c = Circle(3)  # 实例化一个半径为3的圆
    print(c.area())  # 计算半径为3的圆的面积
    print(c.perimeter())  # 计算半径为3的圆的周长


# 7、要求：定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄,性别,家庭住址,爱好等属性；
# 将类中的年龄和家庭住址私有化；
# 提供查看私有属性的方法；
# 提供获取用户信息的方法；
# 提供可以修改私有属性的方法，修改家庭住址和修改年龄(年龄范围：0-100)。
class Person:
    def __init__(self, name, age, gender, address, hobby):
        self.__age = int(age)
        self.__address = address
        self.name = name
        self.gender = gender
        self.hobby = hobby

    def get_age(self):
        return self.__age

    def get_info(self):
        return (f"姓名：{self.name}\n"
                f"年龄：{self.__age}\n"
                f"性别：{self.gender}\n"
                f"家庭住址：{self.__address}\n"
                f"爱好：{self.hobby}")

    def set_age(self, new_age):
        # 先判断输入的年龄是否是整数
        try:
            # 尝试将输入的年龄转换为整数
            new_age = int(new_age)
            # 再判断年龄是否在0-100之间
            if 0 <= new_age <= 100:
                # 如果年龄在范围内，则修改年龄
                self.__age = new_age
            # 否则提示年龄范围不对
            else:
                print("年龄范围必须在0-100之间！")
        # 如果输入的年龄不是整数，则提示年龄必须是整数
        except ValueError:
            print("年龄必须是整数！")

    def set_address(self, new_address):
        self.__address = new_address


if __name__ == "__main__":
    p = Person("小明", 20, "男", "北京", "看书")
    print(p.get_info())  # 打印信息
    p.set_age(25)  # 修改年龄为25
    p.set_address("上海")  # 修改家庭住址为上海
    print(p.get_info())  # 打印修改后的信息
    p.set_age("200")  # 修改年龄为200，提示年龄范围不对
    p.set_address("广州")  # 修改家庭住址为广州
    print(p.get_info())  # 打印修改后的信息


class BankCard:
    def __init__(self, name, card_number, password, balance):
        self.name = name
        self.card_number = card_number
        self.password = password
        self.balance = balance

    def withdraw(self):
        try:
            amount = float(input("请输入取款金额: "))
            if amount > self.balance:
                print("余额不足，取款失败。")
            else:
                self.balance -= amount
                print(f"取款成功，当前余额为: {self.balance:.2f} 元。")
        except ValueError:
            print("输入的金额不是有效的数字，请重新操作。")


class LocalBankCard(BankCard):
    def withdraw(self):
        super().withdraw()

    def transfer(self, target_card):
        try:
            amount = float(input("请输入转账金额: "))
            if amount > self.balance:
                print("余额不足，转账失败。")
            else:
                self.balance -= amount
                target_card.balance += amount
                print(f"转账成功，当前余额为: {self.balance:.2f} 元。")
                print(f"目标账户余额为: {target_card.balance:.2f} 元。")
        except ValueError:
            print("输入的金额不是有效的数字，请重新操作。")


class OtherBankCard(BankCard):
    def withdraw(self):
        try:
            amount = float(input("请输入取款金额: "))
            total_amount = amount + 2
            if total_amount > self.balance:
                print("余额不足，取款失败。")
            else:
                self.balance -= total_amount
                print(f"取款成功，收取 2 元手续费，当前余额为: {self.balance:.2f} 元。")
        except ValueError:
            print("输入的金额不是有效的数字，请重新操作。")


if __name__ == "__main__":
    # 实例化三个类
    bank_card1 = BankCard("张三", "123456", 123456, 10000)
    # 实例化本行卡类
    bank_card2 = LocalBankCard("李四", "654321", 323211, 50000)
    # 实例化其他行卡类
    bank_card3 = OtherBankCard("王五", "123456", 432121, 5000)
    # 调用取款方法
    bank_card1.withdraw()
    bank_card2.withdraw()
    bank_card3.withdraw()
    # 调用转账方法
    bank_card2.transfer(bank_card3)  # 从本地卡转账到其他卡
    # 再次调用转账方法
    bank_card2.transfer(bank_card1)  # 从本地卡转账到银行卡
# 成功实现了银行卡类，可以进行取款和转账操作。
