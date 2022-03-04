import json
import time
from pprint import pprint
from urllib.parse import urlencode
import requests
import re

from lxml import etree
import datetime
from django.template.defaultfilters import striptags

import htmljiexi

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://m.weibo.cn/u/'  # 这个需要改成所要爬取用户主页的手机版本下的url
}

# 4677399825875715

def getgy(urlid):

    id = urlid
    #'https://m.weibo.cn/status/4725600311578496'
    realurl = 'https://m.weibo.cn/status/%s' % (id)
    res = requests.get(realurl, headers=header)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)


    gameList = root.xpath("/html/body/script[1]/text()")
    # print(gameList)
    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
    return list1

def gy(urlid):
    urlid = urlid


    for j in getgy(urlid):
        # print(j)
        objson = json.loads(j)
    return objson

def zhuanjson(urlid):
    urlid = urlid
    h = gy(urlid)
    h = str(h)
    jj = eval(h)
    j = json.dumps(jj)

    return j


def lasttxt(urlid):
    urlid = urlid
    g = zhuanjson(urlid)
    js = json.loads(g)
    dd = js['status']['text']

    content = striptags(dd)
    return content


def lasthtml(urlid):
    urlid = urlid
    g = zhuanjson(urlid)
    js = json.loads(g)
    dd = js['status']['text']

    # content = striptags(dd)
    return dd

global beizhu

def panduanisgy(urlid):
    urlid = urlid
    textwenben=lasttxt(urlid)
    zifu='直播预告'
    zifu2='疫情防控'
    zifu3='新闻发布会'
    if  zifu in textwenben:

        if zifu2 in textwenben:
            if zifu3 in textwenben:

                print('1')
                htmldata = lasthtml(urlid)
                huanghang = "<br />"
                tupianxianshi='<meta name="referrer" content="no-referrer" />'
                tu = htmljiexi.getpiclast(urlid)
                content = htmldata + huanghang + tupianxianshi+tu
                content = content.replace('"','\"')
                content = content.replace('\ "', '\"')

                # print(content)
                url = 'http://wxpusher.zjiecode.com/api/send/message'
                HEADERS = {'Content-Type': 'application/json'}
                # dt = datetime.now()
                # time = dt.strftime('%Y-%m-%d')
                # 'application/x-www-form-urlencoded'
                # 'application/json;charset=utf-8'
                FormData = {
                    "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
                    "content": content,
                    "summary": f"AKB48TeamSH有握手会安排！",
                    "contentType": 2,

                    "topicIds": [

                    ],
                    "uids": [
                        "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
                    ],
                    "url": ""
                }
                # FormData=urlencode(FormData)

                res = requests.post(url=url, json=FormData, headers=HEADERS)
                # content = requests.post(url=url, data=FormData).text

                print(res.text)
            else:
                pass

        else:
            pass



    else:
        print('2')
        pass



# if __name__ == '__main__':
#     panduanisgy(4743267772798739)


def lastfanhui(urlid):
    urlid = urlid
    ddd = panduanisgy(urlid)
    ddd = ddd.replace('\n', '')
    ddd = ddd.replace('\r', '')
    ddd = ddd.replace('\t', '')

    now_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    bd = now_time.strftime('%Y%m%d')

    last_time = datetime.datetime.now() + datetime.timedelta(days=6)
    last_bd = last_time.strftime('%Y%m%d')
    print(last_bd)
    print(bd)
    urlid=str(urlid)
    url='https://m.weibo.cn/status/'+urlid

    # bd='123'
    dd = "[('" + bd + "','" + last_bd + "','" + ddd + "','" + url + "')]"

    dd = eval(dd)
    return dd


# if __name__ == '__main__':
#     gt=lastfanhui(4735294307568601)
#     #4677399825875715
#
#     print(gt)





