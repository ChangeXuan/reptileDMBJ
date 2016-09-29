# -*- coding:utf-8 -*-
 
#--------抓取的基本流程----------#
#1：首先获得基础页的源码
#2：从基础页的源码中提取出每个信息所在的网页
#3：获得信息页的源码
#4：从源码中获取所需内容
#                           D-Day
#---------------------------------
import urllib2
import re
import HttpTool
import time

#通过请求获取HTML源码
def getSource(url):
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1','Referer' : '******'}
    request=urllib2.Request(url,headers = header)
    response=urllib2.urlopen(request)
    source=response.read()
    return source

def getContentUrl(source):
    contents = re.findall('<td><a href="(.*?)">',source,re.S)
    return contents

#解析日报内容
def getContent(url):
    source = getSource(url)
    #打印所需内容
    items_withtag = re.findall('<div style="clear:both"></div>(.*?)<span',source,re.S)
    for item in items_withtag:
        data = HttpTool.Html_tool().replace_char(item.replace("\n",""))
        all_data.append(data)
    

def main():
    url = "http://www.daomubiji.com/"
    source = getSource(url)
    contentUrl = getContentUrl(source)
    flag = 0
    for item in contentUrl:
        getContent(item)
        flag+=1
        if flag == 10 :
            time.sleep(120)
            flag = 0
        print "1"

    f = open("dmbj.txt","w+")
    f.writelines(all_data)
    f.close
 
 
all_data = []
if __name__ == "__main__":
    main()