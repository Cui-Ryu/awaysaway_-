# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 13:25
# @Author  : AWAYASAWAY
# @File    : 图片爬取.py
# @IDE     : PyCharm
# @aim     : 爬取糗事百科图片

import requests

if __name__ == '__main__':
    # 如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12343/123432374/medium/3HVOMHSC7EVVFAAY.jpg'
    # content返回的是二进制形式的图片数据
    # text(字符串)   content(二进制)  json() (对象)
    img_data = requests.get(url=url).content

    # 持久化存储
    with open('./qiutu.jpg', mode='wb') as fp:
        fp.write(img_data)
