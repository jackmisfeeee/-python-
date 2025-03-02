print("             王者荣耀登录界面        ")
print('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')
print('用户登录')
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'tom' and password == '123':
    print('登录成功~')
    print('欢迎来到王者荣耀~')
else:
    print("用户名或者密码输入错误")
# 后续找到方式在输入错误后不执行后续代码
print('1.排位赛')
print('2.皮肤商城')
print('2.万象天工')
module = int(input('请输入你要进入的模块：'))
if module == 1:
    print('')  # 后续搭建
if module == 2:
    print("分类   英雄  名称        金额(点卷)")
    print("勇者   小乔  丁香结       60")
    print("传说   伽罗  太华        1798")
    print("史诗   虞姬  启明星使     5000+")
print('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')
if module == 3:  # 后续搭建
    print('')
chose = (input('请输入你要购买的英雄：'))
if chose == '小乔':
    print("英雄小乔的皮肤购买成功")
elif chose == '伽罗':
    print("英雄伽罗的皮肤购买成功")
elif chose == '虞姬':
    print("英雄虞姬的皮肤购买成功")
