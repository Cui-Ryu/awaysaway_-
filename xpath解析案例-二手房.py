# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 22:54
# @Author  : AWAYASAWAY
# @File    : xpath解析案例-二手房.py
# @IDE     : PyCharm
# @需求     : 爬取58二手房中的房源信息
'''
https://bj.58.com/ershoufang/pn3/?PGTID=0d30000c-0000-1714-2f56-15a9ce35b822&ClickID=1
https://bj.58.com/ershoufang/pn4/?PGTID=0d30000c-0000-1615-7e50-89732bc6e106&ClickID=1
'''
import requests
from lxml import etree
import xlwt


def test():
    # 先爬取页面源码数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # url = 'https://bj.58.com/ershoufang/pn1/?PGTID=0d30000c-0000-1615-7e50-89732bc6e106&ClickID=1'
    url = 'https://bj.58.com/ershoufang/pn%d/?PGTID=0d30000c-0000-1615-7e50-89732bc6e106&ClickID=1'
    # pageNum = 1
    for pageNum in range(1, 30):
        new_url = format(url % pageNum)
        page_text = requests.get(url=new_url, headers=headers).text
        #print(page_text)

        # 数据解析
        tree = etree.HTML(page_text)
        # 存储的是就是li标签对象
        li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')

        # 持久化存储
        fp = open('58.txt', mode='w', encoding='utf8')
        wb = xlwt.Workbook(encoding='utf8')
        ws = wb.add_sheet('Sheet1')
        ws.write(0, 0, label='地点')  # title
        ws.write(0, 1, label='总价/万')  # price
        ws.write(0, 2, label='单价')  # per_price
        ws.write(0, 3, label='房型')  # baseinfo1
        ws.write(0, 4, label='面积')  # baseinfo2
        ws.write(0, 5, label='朝向')  # baseinfo3
        ws.write(0, 6, label='位置')  # baseinfo4

        val = 1
        for li in li_list:
            title = li.xpath('./div[2]/h2/a/text()')[0]
            price = li.xpath('./div[3]/p[1]/b/text()')[0]
            per_price = li.xpath('./div[3]/p[2]/text()')[0]
            baseInfo1 = li.xpath('./div[2]/p[1]/span[1]/text()')[0]
            baseInfo2 = li.xpath('./div[2]/p[1]/span[2]/text()')[0]
            baseInfo3 = li.xpath('./div[2]/p[1]/span[3]/text()')[0]
            baseInfo4 = li.xpath('./div[2]/p[1]/span[4]/text()')[0]

            #print(title, price, per_price, baseInfo1, baseInfo2, baseInfo3, baseInfo4)

            fp.write(title + '\n')
            ws.write(val, 0, title)
            ws.write(val, 1, price)
            ws.write(val, 2, per_price)
            ws.write(val, 3, baseInfo1)
            ws.write(val, 4, baseInfo2)
            ws.write(val, 5, baseInfo3)
            ws.write(val, 6, baseInfo4)

            print(u'......第%d页爬取成功......' % val)

            val += 1

        wb.save('c:\\users\\15301\\desktop\\58二手房信息.xls')
    print(u'......全部结束！！！')


if __name__ == '__main__':
    test()
