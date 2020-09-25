# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 0:03
# @Author  : AWAYASAWAY
# @File    : b站爬虫.py
# @IDE     : PyCharm

'''
爬取B站弹幕数据的API：https://api.bilibili.com/x/v1/dm/list.so?oid=XXX
方法一：获取oid
1. 我们要想知道这个oid是什么，首先要获取到cid。弹幕数据的接口我们虽然找不到，但是目录页接口还是可以找到的，
   网址如下。https://api.bilibili.com/x/player/pagelist?bvid=BV1PK4y1b7dt&jsonp=jsonp   <bvid在b站的视频url中就能找到>
   通过这个网址我们可以获取到我们要的那个cid，cid这个键对应的值，就是我们要的oid数字串
2. 首先，bilibili的弹幕是在xml文件里，每个视频都有其对应的cid和aid，我们取到cid中的数字放入url中
3. 合成url http://comment.bilibili.com/201056987.xml 就可以看到弹幕文件xml  <注：cid=201056987 是专辑《MOJITO》专辑视频的cid>
4. 由于这个MV只有一个完整的视频，所以这里只有一个cid，如果一个视频是分不同小结发布的，这里就会有多个cid，不同的cid代表不同的视频。

方法二：获取oid
1. F12命令
2. 点击 Network
3. Console搜索框中搜索 oid 即可出现数字
'''

import requests
import json
import chardet
import re
import io
from pprint import pprint


# 1.根据bvid请求得到cid
def get_cid():
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1PK4y1b7dt&jsonp=jsonp'
    res = requests.get(url).text
    json_dict = json.loads(res)
    # pprint(json_dict)
    return json_dict["data"][0]["cid"]


# 2.根据cid请求弹幕，解析弹幕得到最终的数据
"""
注意：哔哩哔哩的网页现在已经换了，那个list.so接口已经找不到，但是我们现在记住这个接口就行了。
"""


def get_data(cid):
    final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    final_res = requests.get(final_url)
    final_res.encoding = chardet.detect(final_res.content)['encoding']
    final_res = final_res.text
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    # pprint(final_res)
    return data


# 3.保存弹幕列表
def save_to_file(data):
    with io.open("dan_mu.txt", mode="w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")




if __name__ == '__main__':
    cid = get_cid()
    data = get_data(cid)
    save_to_file(data)
