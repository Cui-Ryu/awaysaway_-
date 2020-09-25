# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 20:23
# @Author  : AWAYASAWAY
# @File    : xpath解析基础.py
# @IDE     : PyCharm


from lxml import etree
import requests

def xpath_test():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }

    # 测试url
    url = 'https://music.163.com/discover/song?id=1468998724'
    page_text = requests.get(url=url, headers=headers).text

    # 实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    parser = etree.HTMLParser(encoding="utf-8")
    html = etree.HTML(page_text, parser=parser)

    # res = tree.xpath('/html/body/div')
    # res = tree.xpath('/html//div')
    # res = tree.xpath('//div')
    # res = tree.xpath('//p[@class="title"]')
    # res = tree.xpath('//div[@class="song"]/p')
    # res = tree.xpath('//div[@class="song"]/p/text()')[0]
    # res = tree.xpath('//div[@class="song"]//text()')  # 全部内容
    # res = tree.xpath('//div[@class="song"]/text()')  # 空格
    # res = tree.xpath('//section[@class="thumb-listing-page"]//a/@href')
    res =html.xpath('//table[@class="m-table"]//div[2]//a//@href')


    print(res)


if __name__ == '__main__':
    xpath_test()

'''
src="https://w.wallhaven.cc/full/5w/wallhaven-5w26x1.jpg"
src="https://w.wallhaven.cc/full/5w/wallhaven-r2k5oq.jpg"
'''