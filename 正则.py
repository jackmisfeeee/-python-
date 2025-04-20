import re

res = re.match('s', 'hello world')
print(res)
res = re.match('h', 'hello world')
print(res)

# re.findall(pattern,string)
res = re.findall('h', 'hello world')
print(res)
res = re.findall('o', 'hello world')
print(res)
res = re.findall('q', 'hello world')
print(res)  # 没匹配则返回空列表

# re.search()方法
res = re.search('q', 'hello')
print(res)
res = re.search('l', 'hello')
print(res)
res = re.search('o', 'hello')
print(res)
# .匹配任意字符
res = re.match('.', '\n&^&*hello world')
print(res)
res = re.search('.', '\nhello')
print(res)
res = re.match('.', '&^&*hello')
print(res.group())
k = res.group()
print('ss' + f'{k}')
res = re.match('[hHfqsr]', 'qHhello world')
print(res)
print(res.group())
res = re.match('[0-9]', '22qHhello world')
print(res)
print(res.group())
res = re.match('[0-57-9]', '97675622qHhello world')
print(res)
print(res.group())
res = re.match('[a-z]', 'a22qHhello world')
print(res)
print(res.group())
res = re.match('[A-Z]', 'Av22qHhello world')
print(res)
print(res.group())
res = re.match('[a-zA-Z]', 'a22qHhello world')
print(res)
print(res.group())
res = re.match(r'\d', '22qHhello world')  # 匹配数字
print(res)
print(res.group())
res = re.match(r'\D', '(\n\ta22qHhello world')  # 非
print(res)
print(res.group())
res = re.match(r'\s', '\n {22qHhello world')  # 匹配空字符
print(res)
print(res.group())
res = re.match(r'\S', r'\-dad+ 111 {22qHhello world')  # 非
print(res)
print(res.group())
res = re.match(r'\w', 'a1哦哦哦 {22qHhello world')  # 匹配单词字符 数字 字母 _ 汉字
print(res)
print(res.group())
res = re.match(r'\W', ' {22qHhello world')  # 非
print(res)
print(res.group())
res = re.match(r'\n', '\n {22qHhello world')
print(res)
print(res.group())
res = re.match(r'\t', '\t {22qHhello world')
print(res)
print(res.group())
res = re.findall(r'\d*', 'q34Hhello21 world')  # 匹配所有数字
print(res)
res = re.findall(r'\d+', 'q34Hhello21 world')  # 匹配所有数字,不为0
print(res)
res = re.findall(r'\d?', 'q34Hhello21_ world')  # 匹配所有数字,不为0
print(res)
res = re.findall(r'\d{1,3}', 'q33334Hhel1lo21 world')  # 匹配所有数字,不为0
print(res)
res = re.findall(r'l{1,3}', 'q33334Hhel1lo21 world')
print(res)
# res = re.findall(r'^oou?', 'oouioo00q33334Hhel1lo21 world')
# print(res)
res = re.findall(r'[^hH]+', 'oouioo0heHH0q33334Hhel1lo21 world')  # 取反 匹配除hH外的所有字符
print(res)
# ['oouioo0', 'e', '0q33334', 'el1lo21 world']
# 类似分隔操作split 以hH作为分隔符
res = re.findall(r'\w$', 'q34Hhello21 world')
print(res)
res = re.match(r'\w+\s(\w+$)', 'q34Hhello21 world')
print(res)

print(res.group(1))

res = re.match(r'\w{5,11}@qq\.com', '1236192678@qq.com')
print(res)
res = re.match(r'\w{5,11}@(qq|126|163|outlook)\.com', '1236192678@qq.com')
print(res)
print(res.group(1))
res = re.match(r'\w{5,11}@(qq|126|163|outlook)\.com', '1236192678@163.com')
print(res)
print(res.group(1))
#  匹配手机号
str1 = '电话信息：135478741125, 12524741554, 18547112545, 15201444178'
pattern = r'1[3-9]\d{9}'
res = re.findall(pattern, str1)
# 开头必须是1
# 1后面的数字必须是3-9的
print(res)
