# 字符串是一种常见的数据容器
# 可以通过下标索引
string = "天涯何处觅芳草"
# 正向索引(下标):从0开始从左往右
# 反向下标（索引）：从负一开始从右往左
print(string[0])  # 天 第0号下标的元素
print(string[1])  # 涯
print(string[3])  # 何
print(string[4])  # 觅
print(string[5])  # 芳
print(string[6])  # 草
# 下标不能超出范围调用，否则会报错
# print(string[7])  # IndexError: string index out of range
# 用反向索引依次输出字符串中的内容
print(string[-7])
print(string[-6])
print(string[-5])
print(string[-4])
print(string[-3])
print(string[-2])
print(string[-1])
string = "天涯何处觅芳草"
#         天  涯  何  处  觅  芳  草
#         0   1   2   3   4   5  6
#        -7  -6  -5  -4  -3  -2  -1
# 字符串切片： 索引的扩展操作，可以选择截取字符串中的内容
print(string[0::])  # [start： stop： 步长]
print(string[1:5:1])  # 涯何处觅
print(string[0:5:2])  # 天何觅
# 也遵循包前不包后原则
print(string[-1::-1])  # 逆序
# 范围可以超出 不影响截取
print(string[:100:1])
print(string[-7:])  # 负向下标切片
