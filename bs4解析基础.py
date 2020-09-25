# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 20:27
# @Author  : AWAYASAWAY
# @File    : bs4解析基础.py
# @IDE     : PyCharm


from bs4 import BeautifulSoup


def test():
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', mode='r', encoding='utf8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.div)  # soup.tagName 返回的是html中第一次出现的tagName标签
    # find('tagName')：等同于soup.div
    # print(soup.find('div'))  # 相当于 soup.div
    # print(soup.find('p', class_='story'))
    # print(soup.find('a', id='link2'))
    # print(soup.find_all('a'))
    # print(soup.select('.title'))
    # print(soup.select('.story > a')[0].get_text())
    # print(soup.find('p', class_='story').text)
    # print(soup.find('p', class_='story').string)   # 直系下为None
    print(soup.select('.story > a')[0]['href'])


if __name__ == '__main__':
    test()
