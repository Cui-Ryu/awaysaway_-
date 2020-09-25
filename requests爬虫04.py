# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 19:03
# @Author  : AWAYASAWAY
# @File    : requests爬虫04.py
# @IDE     : PyCharm


import requests
import json
import xlwt

# --------------爬取豆瓣喜剧电影排行榜-------------- #
if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 指定url
    # 如果想换类型，点击相应的url，然后删去?及后面的参数，换成参数列表
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 从库中的第几部电影去取。0：表示从当前页面第一个文件开始存储
        'limit': '200',  # 一次取出的个数，可自行修改limit
    }

    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()

    # 存文件路径
    file_path = './douban.json'
    fp = open(file_path, 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!!!')

# --------------解析douban.json为excel.-------------- #
    # 创建excel工作表
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    # 设置表头
    ws.write(0, 0, label='rank')
    ws.write(0, 1, label='score')
    ws.write(0, 2, label='types')
    ws.write(0, 3, label='regions')
    ws.write(0, 4, label='title')
    ws.write(0, 5, label='release_date')
    ws.write(0, 6, label='vote_count')
    ws.write(0, 7, label='actors')
    ws.write(0, 8, label='url')

    # 读取json文件
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = json.load(fp)

    # 将json字典写入excel
    val = 1
    for list_item in data:
        for key, value in list_item.items():
            if key == 'rank':
                ws.write(val, 0, value)
            elif key == 'score':
                ws.write(val, 1, value)
            elif key == 'types':
                ws.write(val, 2, value[0])
            elif key == 'regions':
                ws.write(val, 3, value[0])
            elif key == 'title':
                ws.write(val, 4, value)
            elif key == 'release_date':
                ws.write(val, 5, value)
            elif key == 'vote_count':
                ws.write(val, 6, value)
            elif key == 'actors':
                ws.write(val, 7, value[:])
            elif key == 'url':
                ws.write(val, 8, value)
        print(u'......正在写入第%s行' % val)
        val += 1

    # 保存excel文件
    print(u'......保存成功！！！')
    wb.save('./douban.csv')
