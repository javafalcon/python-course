from NetSpider import *
import json
import re

def getImg(html):
    imgre = re.compile('"thumbURL":"(.*?)"')
    imglist = re.findall(imgre,html)
    return imglist

def download(urls,path):
    index = 1
    for url in urls:
        print("Download Image from page:{}".format(url))
        status = downloadImageFile(url,path,str(index)+".jpg")
        try:
            if str(status)[0] == '4':
                print("未下载成功{}".format(url))
                continue
        except Exception as e:
            print("未下载成功{}".format(url))
        index += 1


page = 'https://image.baidu.com/search/index?tn=baiduimage&word=杨幂'

html= getHTMLText(page)
download(getImg(html), 'e:/baidupic')

