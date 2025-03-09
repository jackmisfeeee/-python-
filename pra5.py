# 1、判断一个数是否为偶数。
num = int(input('输入一个数：'))
if 0 == num % 2:
    print(num, '是偶数', sep='')
else:
    print('%d不是偶数' % num)
# 2、商品折扣计算，某商店消费满200打95折，消费满500打9折，消费满1000打8折，消费满2000打7折（需要格式化输出）。
consumption = int(input('消费金额：'))
if 200 <= consumption < 500:
    consumption *= 0.95
    print("消费满200，打95折，折后价为%d" % consumption)

elif 500 <= consumption < 1000:
    consumption *= 0.90
    print("消费满500，打9折，折后价为%d" % consumption)

elif 1000 <= consumption < 2000:
    consumption *= 0.8
    print("消费满1000，打8折，折后价为%d" % consumption)

elif 2000 <= consumption:
    consumption *= 0.7
    print("消费满2000，打7折，折后价为%d" % consumption)
else:
    print("您不满足活动折扣条件")
# 3、某工厂将在三周年庆典之际，向员工发放奖金。对于工龄超过两年且工资高于5000元的员工，将发放2000元奖金；对于工龄超过两年且工资超过10000元的员工，将发放3000元奖金。对于不符合上述工龄和工资要求的员工，将发放1000元奖金。
working_age = int(input('输入你的工龄（提示：？年）：'))
salary = int(input('输入你的工资（提示：？元/月）：'))
if working_age > 2:
    if salary > 10000:
        bonus = 3000
        print(f"你的奖金为：{bonus}")

    elif salary > 5000:
        bonus = 2000
        print(f"你的奖金为：{bonus}")

    else:
        bonus = 1000
        print(f"你的奖金为：{bonus}")

else:
    bonus = 1000
    print(f"你的奖金为：{bonus}")