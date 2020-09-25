# awaysaway_-
爬虫的学习和案例
## requests模块
- python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。
- 作用：模拟浏览器发请求。

## 如何使用：（requests模块的编码流程）
- 指定url
  - UA伪装
  - 请求参数的处理
- 发起请求
- 获取响应数据
- 持久化存储

环境安装：
- pip install requests

## 实战编码：
- 需求：爬取百度指定词条对应的搜索结果页面（简易网页采集器）
  - UA检测
  - UA伪装
- 需求：破解百度翻译
  - post请求（携带了参数）
  - 响应数据是一组json数据
- 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据
  
- 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数

- 需求：爬取国家药品监督管理总局基于中华人民共和国化妆品生产许可证相关数据
  - http://scxk.nmpa.gov.cn:81/xk/
  - 动态加载数据
  - 首页中对应的企业信息数据是通过ajax动态请求到的
  - http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ff83aff95c5541cdab5ca6e847514f88
  - http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=2e18c9bf5f104197b604a5e02118713c
  - 通过对详情页url的观察发现
    - url的域名都是一样的，只有携带的参数(id)不一样
    - id值可以从首页对应的ajax请求到的json串中得到
    - 域名和id值拼接成一个完整的企业对应的详情页的url
  - 详情页的企业数据也是动态加载出来的
    - http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    - http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    - 观察后发现:
      - 所有post请求的url都是一样的，只有参数id值是不同的
      - 如果我们可以批量获取多家企业的id，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url
      

## 数据解析
- 聚焦爬虫
- 正则
- bs4
- xpath




## bs4解析
使用流程：       
    - 导包：from bs4 import BeautifulSoup
    - 使用方式：可以将一个html文档，转化为BeautifulSoup对象，然后通过对象的方法或者属性去查找指定的节点内容
        （1）转化本地文件：
             - soup = BeautifulSoup(open('本地文件'), 'lxml')
        （2）转化网络文件：
             - soup = BeautifulSoup('字符串类型或者字节类型', 'lxml')
        （3）打印soup对象显示内容为html文件中的内容
## 基础巩固：
    （1）根据标签名查找
        - soup.a   只能找到第一个符合要求的标签
    （2）获取属性
        - soup.a.attrs  获取a所有的属性和属性值，返回一个字典
        - soup.a.attrs['href']   获取href属性
        - soup.a['href']   也可简写为这种形式
    （3）获取内容
        - soup.a.string
        - soup.a.text
        - soup.a.get_text()
       【注意】如果标签还有标签，那么string获取到的结果为None，而其它两个，可以获取文本内容
    （4）find：找到第一个符合要求的标签
        - soup.find('a')  找到第一个符合要求的
        - soup.find('a', title="xxx")
        - soup.find('a', alt="xxx")
        - soup.find('a', class_="xxx")
        - soup.find('a', id="xxx")
    （5）find_all：找到所有符合要求的标签
        - soup.find_all('a')
        - soup.find_all(['a','b']) 找到所有的a和b标签
        - soup.find_all('a', limit=2)  限制前两个
    （6）根据选择器选择指定的内容
               select:soup.select('#feng')
        - 常见的选择器：标签选择器(a)、类选择器(.)、id选择器(#)、层级选择器
            - 层级选择器：
                div .dudu #lala .meme .xixi  下面好多级
                div > p > a > .lala          只能是下面一级
        【注意】select选择器返回永远是列表，需要通过下标提取指定的对象
## xpath 解析
- xpath解析原理
  - 实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象中
  - 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
- 环境的安装
  - pip install lxml
- 如何实例化一个etree对象：from lxml import etree
  - 将本地的html文档中的源码数据加载到etree对象中
    - etree.parse(filePath)
  - 将从互联网上获取的源码数据加载到该对象中
    - etree.HTML('page_text')
  - xpath('xpath表达式')
- xpath表达式：返回的是一个列表
  - / ：表示的是从根节点开始定位。表示的是一个层级。
  - // ： 表示的是多个层级。可以表示从任意位置开始定位。
  - 属性定位：//div[@class='song'] ： tag[@attrName="attrValue"]
  - 索引定位：//div[@class='song']/p[3] ： 索引是从1开始的
  - 取文本：
    - /text() ：获取的是标签中直系文本内容
    - //text() ：标签中非直系的文本内容
  - 取属性：
    - //div[@class="song"]/img/@src ：/@attrName ==>img/@src
爬虫在使用场景中的分类
- 通用爬虫：抓取系统重要组成部分。抓取的是一整张页面数据。
- 聚焦爬虫：是建立在通用爬虫基础之上。抓取的是页面中特定的局部内容。
- 增量式爬虫：检测网站中数据更新的情况。只会抓取网站中最新更新出来的数据。

## 爬虫的矛与盾

反爬机制：门户网站，可以通过制定相应的策略或者技术手段，防止爬虫程序进行网站数据的爬取。

反反爬策略：爬虫程序可以通过制定相关的策略或者技术手段，破解门户网站中具备的反爬机制，从而可以获取门户网站数据。

维基百科：https://zh.wikipedia.org/wiki/Robots.txt

## http协议
- 概念：就是服务器和客户端进行数据交互的一种形式。

常用的请求头信息
- User-Agent：请求载体的身份标识
- Connection：请求完毕后是断开连接还是保持连接

常用的响应头信息
- Content-Type：服务器响应回客户端的数据类型

https协议
- 安全的http或超文本传输协议

加密方式
- 对称密钥加密
- 非对称密钥加密
- 证书密钥加密

