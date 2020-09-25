#-*- coding: utf-8 -*-
# @Time    : 2020/9/3 17:00
# @Author  : AWAYASAWAY
# @File    : requests爬虫_实习僧.py
# @IDE     : PyCharm

import requests

if __name__ == '__main__':
    # 抓取页面
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'https://www.shixiseng.com/interns?page={i}&keyword=%E7%A4%BE%E7%BE%A4%E8%BF%90%E8%90%A5&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
    for i in range(1, 5):
        response = requests.get(url=url, headers=headers)
        page_text = response.text
        print(page_text)

