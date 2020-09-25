# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 16:38
# @Author  : AWAYASAWAY
# @File    : requests爬虫02.py
# @IDE     : PyCharm
# @TODO    : 简易网页采集器


'''
UA：User-Agent（请求载体的身份标识）
UA伪装：门户网站的服务器会检测对应请求的载体身份标识，
       如果检测到请求的载体身份标识为某一款浏览器，说明该请求是一个正常的请求。
       但是，如果检测到请求的载体身份标识不是基于某一款浏览器，则标识该请求是不正常的请求（爬虫）
       则服务器端很有可能拒绝该次请求
'''

import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'https://www.baidu.com/s?'
    # 处理url携带的参数：封装到字典中
    kw = input('输入关键词：')
    param = {
        'wd': kw
    }
    # 对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    # 获取数据
    page_status_code = response.status_code
    page_text = response.text
    # 写入文件
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
