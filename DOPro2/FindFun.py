# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
from lxml import etree
from Resulter import Result
import time


HeaderDict = {# 编好的头消息，防止和谐爬虫
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive'
}


# https://m.zhongziso.com/list/NAME/PAGE
def GetFromZhongzisou(name):# 从种子搜获得信息
    FindingOverFlag = False
    names = []
    sizes = []
    times = []
    mages = []

    # print(url)
    cnt = 1
    while FindingOverFlag == False:
        #制作url
        url = "https://m.zhongziso.com/list/" + urllib.parse.quote(name) + "/" + str(cnt)
        # FindingOverFlag = True
        # 获得页面内容
        cnt += 1
        Request = urllib.request.Request(url,headers = HeaderDict)
        try:
            Response = urllib.request.urlopen(Request)
        except:
            FindingOverFlag = True
            break
        Text = Response.read().decode("utf-8")
        html = etree.HTML(Text)

        # 当网页无法访问时/访问的页数超过原有的页数
        if "error-main" in Text:
            FindingOverFlag = True
            break

        # 分析网页
        TempNames = html.xpath("/html/body/div[1]/div/div[5]/div[2]/ul/li[1]/a[1]")
        TempSizes = html.xpath("/html/body/div[1]/div/div[5]/div[2]/ul/li[2]/dl[1]/dd[2]/text()")
        TempTimes = html.xpath("/html/body/div[1]/div/div[5]/div[2]/ul/li[2]/dl[1]/dd[3]/text()")
        TempMages = html.xpath("/html/body/div[1]/div/div[5]/div[2]/ul/li[2]/dl[2]/a[1]/@href")
        for _name,_size,_time,_mage in zip(TempNames,TempSizes,TempTimes,TempMages):
            names.append(_name.xpath("string(.)"))
            sizes.append(_size)
            times.append(_time)
            mages.append(_mage)
        # time.sleep(10)

    return names,sizes,times,mages
    # ob.names = names
    # ob.sizes = sizes
    # ob.times = times
    # ob.mages = mages

def GetInfo(name,ob):# 最终获得所有信息
    names = []
    sizes = []
    times = []
    mages = []
    TempNames,TempSizes,TempTimes,TempMages = GetFromZhongzisou(name)
    names.extend(TempNames)
    sizes.extend(TempSizes)
    times.extend(TempTimes)
    mages.extend(TempMages)

    # return names,sizes,times,mages
    ob.names.extend(names)
    ob.sizes.extend(sizes)
    ob.times.extend(times)
    ob.mages.extend(mages)



if __name__ == '__main__':
    a,b,c,d = GetFromZhongzisou("使命召唤")
    for i,j,k,l in zip(a,b,c,d):
        print("%s %s %s %s" % (i,j,k,l))
