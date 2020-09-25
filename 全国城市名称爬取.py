# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 9:34
# @Author  : AWAYASAWAY
# @File    : 全国城市名称爬取.py
# @IDE     : PyCharm
# @URL     : https://www.aqistudy.cn/historydata/


import requests
from lxml import etree
import xlrd


def test():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url, headers=headers).text
    # tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # # 热门城市的名称
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     # print(hot_city_name)
    #     all_city_names.append(hot_city_name)
    #
    # # 解析全部城市的名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    #     # print(city_name)
    # print(all_city_names, '\n', len(all_city_names))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # 解析到热门城市和所有城市对应的a标签
    # //div/ul/li/a  热门城市a标签的层级关系
    # //div/ul/div[2]/li/a  全部城市a标签层级关系
    # 存储全部城市的a_list
    all_city_names = []
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div/ul/div[2]/li/a')  # 使用或 |
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
        print(all_city_names, len(all_city_names))


if __name__ == '__main__':
    test()
