# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 20:16
# @Author  : AWAYASAWAY
# @File    : 地名获取经纬度.py
# @IDE     : PyCharm


from geopy.geocoders import Nominatim
import warnings

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

path =
location_data = pd.DataFrame(pd.read_excel(path))
location_name = location_data['location']

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

l1_name = []


def get_location(location):
    gaode_api_url = "https://restapi.amap.com/v3/geocode/geo?address=" + str(
        location) + "&output=XML&key=5ffb29f6dfb07ce65ff4fd7424798a85"
    response = requests.get(gaode_api_url, headers=headers)
    Soup = BeautifulSoup(response.content, 'lxml')
    l1 = Soup.find('location')
    if Soup.location == None:
        print("查询点：{0},坐标为：{1}".format(str(location), 0))
    else:
        print("查询点：{0},坐标为：{1}".format(str(location), l1.text))
    if Soup.location == None:
        l1_name.append([str(location), 0])
    else:
        l1_name.append([str(location), l1.text])

# ------测试----------
# loc = "乌鲁木齐市人民政府"
# get_location(loc)
# ------测试----------
