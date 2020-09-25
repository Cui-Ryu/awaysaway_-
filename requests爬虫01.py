# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 16:20
# @Author  : AWAYASAWAY
# @File    : requests爬虫01.py
# @IDE     : PyCharm


import requests


if __name__ == '__main__':
    # 指定url
    url = 'https://www.csdn.net/'
    # 发起请求：get方法会返回一个响应对象
    response = requests.get(url=url)
    # 获取页面响应数据：text返回的是字符串形式的响应数据
    status_code = response.status_code
    print(status_code)
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./csdn.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束!!!')
