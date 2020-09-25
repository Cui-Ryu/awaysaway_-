# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 19:54
# @Author  : AWAYASAWAY
# @File    : requests爬虫03.py
# @IDE     : PyCharm


import requests
import json

if __name__ == '__main__':
    # 指定url
    post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # post请求参数处理（同get请求一致）
    query = input('请输入查询的英文单词：')
    data = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'simple_means_flag': '3',
        'sign': '17484.305021',
        'token': '76abe245d219111d4cb63432d84a260d',
        'domain': 'common',
    }
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据：json()方法返回的是obj（如果确认响应数据是json类型的，才可以使用json类型）
    page_status = response.status_code
    print('状态代码：', page_status)
    dic_obj = response.json()
    print(dic_obj)
    # 持久化存储
    fileName = query + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('over!!!')
    print(dic_obj)
