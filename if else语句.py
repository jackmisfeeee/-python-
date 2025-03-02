my_score = int(input('请输入你的成绩'))
if my_score >= 60:
    print("你的成绩及格了")
    if my_score >= 80:
        print("优秀")
    elif my_score == 100:
        print("满分！good！")
else:
    print("你的成绩不合格")
    if my_score <= 40:
        print("无药可救。。。")
    else:
        print("还能抢救一下")
# 三目操作符  ： a if 判断式 b  顺序：先执行if判断，若为True，执行a；若为False，执行b
num1 = int(input('请输入第一个数字:'))
num2 = int(input('请输入第二个数字:'))
max_num = num1 if num1 > num2 else num2
print(f"最大的数是：{max_num}")
