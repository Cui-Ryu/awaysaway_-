# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 14:47
# @Author  : AWAYASAWAY
# @File    : requests爬虫06.py.py
# @IDE     : PyCharm


import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/'

    param = {
        'on': 'true',
        'page': '2',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    response = requests.post(url=url, headers=headers, params=param)
