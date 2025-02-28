import keyword

print("Hello world")
# 在控制台显示hello world
print("你好，世界！")
# 在控制台显示你好世界
print("我是一个程序⚪ 哈 哈 哈")
# 同上
print('这一刻 世界静止了 万千的思绪涌入脑中 汇聚成一句话 ：“开始了!”')
# 同上
# 多行注释用三对引号包围
"""
Process finished with exit code 
"""
# python语法规范：
# 1.print(*values, sep' ', end'\n')
# print 在python中是以函数形式存在 必须加（）；（）中的参数有*values，sep，end
"""
    value之间用','隔开并且逗号后要加空格' '
    sep 
        含义：separate .v 分开；分离；独立；区分开；区别开 
        作用：分隔多个value，默认使用sep=' ',即默认以空格分隔开
    end 
        含义： .n 结束;结果；结尾
        作用：设定以什么方式结尾，默认使用end='\n',即默认以换行结尾
"""
# example：

print("hello world", "哈哈哈")
print("hello world", "哈哈哈", sep=",", end='!')
# 将多个值之间的间隔符改为，  将结尾改成！
print("hello world", "哈哈哈", sep=",", end='!')
# 重复操作一遍
print(end='\n')
# 换行
print(keyword.kwlist)
high = 175.22
print(high, type(high))

