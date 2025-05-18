import requests

# 设置程序入口
if __name__ == '__main__':
    # 1获取目标url:
    url_ = 'http://www.ujxsw.org/login.php?do=submit'

    # 2.设置请求头
    headers_ = {
        # 添加用户代理
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    # 设置表单数据
    form_data = {
        'LoginForm[username]': 'Tom',  # 正确用户名
        'LoginForm[password]': '123456789',  # 正确密码
        'submit': '登录',
        'action': 'login'
    }
    # 3.发送post请求 固定关键字参数data=表单数据，携带表单数据获取响应数据
    response_ = requests.post(url=url_, data=form_data, headers=headers_)
    # 4.获取响应数据
    str_data = response_.content.decode('utf-8')
    # 5.打印响应数据
    print(str_data)
