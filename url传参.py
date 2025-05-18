from fake_useragent import FakeUserAgent
import random
import requests

UA = FakeUserAgent().random
print(f'没有发送请求前获取的随机UA:', UA)
print('*'*80)
if __name__ == '__main__':
    url_ = 'https://www.baidu.com'
    headers_ = {'User-Agent': UA}
    response = requests.get(url=url_, headers=headers_)
# 打印百度服务器检测到的我们所使用的UA身份
    print('百度服务器检测到的我们的UA身份:', response.request.headers)

