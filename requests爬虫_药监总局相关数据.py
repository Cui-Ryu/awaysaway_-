# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 5:09
# @Author  : AWAYASAWAY
# @File    : requests爬虫_药监总局相关数据.py
# @IDE     : PyCharm

import requests
import json
import xlwt

if __name__ == '__main__':
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 存储
    id_list = []  # 存放企业id
    all_data_list = []  # 存储所有企业的详情数据
    # 参数的封装
    for page in range(1, 5):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        # 字典类型
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        page_status_code = requests.status_codes

        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        #print(detail_json, '----------ending-----------')
        all_data_list.append(detail_json)

    # 持久化存储为json
    fp = open('./all_data.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)

    # # 持久化存储为excel
    # # 读取json文件
    # with open('all_data.json', mode='r', encoding='utf-8') as fp:
    #     json_data = json.load(fp)
    #
    # wb = xlwt.Workbook(encoding='utf-8')
    # ws = wb.add_sheet('sheet1')
    # # 设置表头
    # ws.write(0, 0, label='epsName')
    # ws.write(0, 1, label='productSn')
    # ws.write(0, 2, label='certStr')
    # ws.write(0, 3, label='epsAddress')
    # ws.write(0, 4, label='epsProductAddress')
    # ws.write(0, 5, label='businessLicenseNumber')
    # ws.write(0, 6, label='legalPerson')
    # ws.write(0, 7, label='businessPerson')
    # ws.write(0, 8, label='qualityPerson')
    # ws.write(0, 9, label='qfManagerName')
    # ws.write(0, 10, label='xkName')
    # ws.write(0, 11, label='rcManagerDepartName')
    # ws.write(0, 12, label='rcManagerUser')
    # ws.write(0, 13, label='xkDate')
    # ws.write(0, 14, label='xkDateStr')
    # # 将detail_json写入excel
    # val = 1
    # for data_item in json_data:
    #     for key, value in data_item.items():
    #         if key == 'epsName':
    #             ws.write(val, 0, value)
    #         elif key == 'productSn':
    #             ws.write(val, 1, value)
    #         elif key == 'certStr':
    #             ws.write(val, 2, value)
    #         elif key == 'epsAddress':
    #             ws.write(val, 3, value)
    #         elif key == 'epsProductAddress':
    #             ws.write(val, 4, value)
    #         elif key == 'businessLicenseNumber':
    #             ws.write(val, 5, value)
    #         elif key == 'legalPerson':
    #             ws.write(val, 6, value)
    #         elif key == 'businessPerson':
    #             ws.write(val, 7, value)
    #         elif key == 'qualityPerson':
    #             ws.write(val, 8, value)
    #         elif key == 'qfManagerName':
    #             ws.write(val, 9, value)
    #         elif key == 'xkName':
    #             ws.write(val, 10, value)
    #         elif key == 'rcManagerDepartName':
    #             ws.write(val, 11, value)
    #         elif key == 'rcManagerUser':
    #             ws.write(val, 12, value)
    #         elif key == 'xkDate':
    #             ws.write(val, 13, value)
    #         elif key == 'xkDateStr':
    #             ws.write(val, 14, value)
    #     print(u'......正在写入%s行' % val)
    #     val += 1
    # print(u'......保存成功!!!')
    # wb.save('detail_json.xls')

    print('over!!!')



