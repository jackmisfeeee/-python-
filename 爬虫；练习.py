# 导入requests库
import requests
from fake_useragent import FakeUserAgent

# 设置程序入口
if __name__ == '__main__':
    # 1获取目标url:
    url = 'http://www.ujxsw.org/modules/article/bookcase.php'
    UA = FakeUserAgent().random
    # 2.设置请求头
    headers_ = {
        # 添加用户代理
        'User-Agent': UA,
        # 添加cookie
        'Cookie': 'username=User; t=57357262627768289dfe62ad9; Hm_lvt_b004b494e9626c54dae768fe71762e1c=1747492183,1747534888; HMACCOUNT=5DF91694BE9A9E65; Hm_lpvt_b004b494e9626c54dae768fe71762e1c=1747535278'
    }

    # 3.发送请求
    # 可以看到除了url是字符串，headers和cookies都是字典传入参数
    response_ = requests.get(url=url, headers=headers_)
    # 4.获取响应数据
    str_data = response_.content.decode('utf-8')
    # 5.打印响应数据
    print(str_data)
