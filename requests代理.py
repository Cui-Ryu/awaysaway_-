# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 13:56
# @Author  : AWAYASAWAY
# @File    : requests代理.py
# @IDE     : PyCharm


import requests


def test():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'https://www.baidu.com/s?wd=ip'
    # 182.34.27.129:9999 , proxies={'https://': '112.115.57.20:3128'}
    page_text = requests.get(url=url, headers=headers).text

    with open('ip.html', mode='w', encoding='utf8') as fp:
        fp.write(page_text)


if __name__ == '__main__':
    test()
