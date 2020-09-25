# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 18:18
# @Author  : AWAYASAWAY
# @File    : requests爬虫_高德交通.py
# @IDE     : PyCharm


import requests
import json
import xlwt
import pandas as pd
import csv


def getCityInfo():
    '''
    获取城市代码：code
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 指定url
    url = 'https://trp.autonavi.com/ajax/getCityInfo.do?'
    response = requests.get(url=url, headers=headers)
    page_status_code = response.status_code
    print(page_status_code)
    page_json = response.json()
    fp = open('getCityInfo.json', 'w', encoding='utf-8')
    json.dump(page_json, fp=fp, ensure_ascii=False)
    # print(page_json)
    print(u'...高德交通页面文件抓取，保存成功!!!')

    # 写入excel文件
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    ws.write(0, 1, label='code')
    ws.write(0, 0, label='name')
    ws.write(0, 2, label='pinyin')

    with open('getCityInfo.json', mode='r', encoding='utf-8') as fp:
        data = json.load(fp)

    val = 1
    for line in data:
        for key, value in line.items():
            if key == 'code':
                ws.write(val, 1, value)
            if key == 'name':
                ws.write(val, 0, value)
            if key == 'pinyin':
                ws.write(val, 2, value)
        # print(u'...正在写入第%s行：' % val)
        val += 1

    save2file = 'getCityInfo.xls'
    print(u'...文件保存成功%s' % save2file)
    wb.save(save2file)

    df = pd.read_excel(save2file)
    city_code_query = input('输入城市名，查询代码：')
    city_code = df[df['name'] == city_code_query]['code'].values[0]
    # print(city_code)
    return city_code


def getCityRoad(city_code):
    ''' 未来一周拥堵预测 '''
    # 指定url=https://trp.autonavi.com/ajax/getCityRoadTop.do?adcode=440400&date=2020-09-03
    url = 'https://trp.autonavi.com/ajax/getCityRoadTop.do'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    city_code = getCityInfo()
    date = '2020-09-03'
    param = {
        'adcode': city_code,
        'date': date,
    }
    reponse = requests.get(url=url, params=param, headers=headers)
    status_code = reponse.status_code
    print(status_code)
    page_json = reponse.json()
    fp = open('getCityRoad.json', 'w', encoding='utf-8')
    json.dump(page_json, fp=fp, ensure_ascii=False)
    print(u'...拥堵预测页面文件抓取，保存成功!!!')

    # 写入excel文件
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    ws.write(0, 0, label='ranking')
    ws.write(0, 1, label='cityName')
    ws.write(0, 2, label='dir')
    ws.write(0, 3, label='lnglats')
    ws.write(0, 4, label='index')
    ws.write(0, 5, label='speed')

    with open('getCityRoad.json', 'r', encoding='utf-8') as fp:
        data = json.load(fp)

    val = 1
    for line in data:
        for key, value in line.items():
            if key == 'ranking':
                ws.write(val, 0, value)
            if key == 'cityName':
                ws.write(val, 1, value)
            if key == 'dir':
                ws.write(val, 2, value)
            if key == 'lnglats':
                ws.write(val, 3, value)
            if key == 'index':
                ws.write(val, 4, value)
            if key == 'speed':
                ws.write(val, 5, value)
        print(u'正在读取第%s行' % val)
        val += 1
    wb.save('getCityRoad.xls')
    print(u'文件保存成功：%s' % 'getCityRoad.xls')


if __name__ == '__main__':
    city_code = getCityInfo()
    getCityRoad(city_code)
