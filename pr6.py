# 例1：小黑喜欢小美，每天都去向小美表白，直到表白成功！小美比较心软，只需要小黑表白99次。小黑每次表白的流程：先送十朵玫瑰花，然后再跟小美表白。
# for 循环实现：
# for i in range(1, 100):
#     print(f"今天是表白的第{i}天")
#     for k in range(11):
#         print(f"送给小美第{k}朵花")
#     print(f"小美我喜欢你！")
# print("小黑表白成功!")

# 例2：打印九九乘法表
# 会打印9行内容
# 每一行的内容，跟行数有关系
print(1)
for i in range(1, 10):
    for j in range(1, i + 1):
        # if i == 3 and j == 3:
        #     print(end=" ")
        # elif i == 4 and j == 3 or j == 4:
        #     print(end=" ")
        print(f"{i}x{j}={i * j}", end=' ')
    print()
# 实现。
print()
print(2)
# while 嵌套实现：
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(f"{i}x{j}={i * j}", end=' ')
        j += 1
    print()
    i += 1
print()
print(3)
# 反向实现：
for i in range(9, 0, -1):
    for j in range(1, i+1, 1):
        print(f"{i}x{j}={i * j}", end=' ')
    print()
