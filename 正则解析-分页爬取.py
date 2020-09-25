# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 17:08
# @Author  : AWAYASAWAY
# @File    : 正则解析-分页爬取.py
# @IDE     : PyCharm


import requests
import re
import os


def getImage():
    # 创建一个文件夹，保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    # pageNum = 1
    for pageNum in range(1, 14):
        # 对应页码的url
        new_url = format(url % pageNum)

        # 使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text

        # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)  # re.S单行匹配
        # print(img_src_list)
        print(u'............正在下载第%s页图片' % pageNum)

        for src in img_src_list:
            # 拼接出一个完整图片的url
            src = 'https:' + src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储路径
            img_path = './qiutuLibs/' + img_name
            with open(img_path, mode='wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！！')
    print(u'...........图片下载结束!!!')


if __name__ == '__main__':
    getImage()
