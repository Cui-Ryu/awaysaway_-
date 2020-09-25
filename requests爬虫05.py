# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 21:17
# @Author  : AWAYASAWAY
# @File    : requests爬虫05.py
# @IDE     : PyCharm


import requests
import json
import xlwt

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    kw = input('输入查询地点：')
    param = {
        'cname': '',
        'pid': '',
        'keyword': kw,  # 地点查询参数
        'pageIndex': '1',
        'pageSize': '100',  # 更改页面列表长度
    }
    response = requests.post(url=url, params=param, headers=headers)
    page_status_code = response.status_code
    print(page_status_code)
    page_text = response.json()
    fileName = kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(page_text, fp=fp, ensure_ascii=False)
    print('保存成功!!!')
    print(page_text)

    # 解析json数据
    # 创建excel工作表
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    # 设置表头
    ws.write(0, 0, label='rownum')
    ws.write(0, 1, label='storeName')
    ws.write(0, 2, label='addressDetail')
    ws.write(0, 3, label='pro')
    ws.write(0, 4, label='provinceName')
    ws.write(0, 5, label='cityName')

    # 读取json文件
    with open(fileName, mode='r', encoding='utf-8') as fp:
        data = json.load(fp)['Table1']
    # 将json字典写入excel
    val = 1
    for data_item in data:
        for key, value in data_item.items():
            if key == 'rownum':
                ws.write(val, 0, value)
            if key == 'storeName':
                ws.write(val, 1, value)
            if key == 'addressDetail':
                ws.write(val, 2, value)
            if key == 'pro':
                ws.write(val, 3, value)
            if key == 'provinceName':
                ws.write(val, 4, value)
            if key == 'cityName':
                ws.write(val, 5, value)
        print(u'......正在写入第%s行' % val)
        val += 1
    # 保存csv文件
    print(u'......保存成功！！！')
    wb.save(kw + '.csv')
