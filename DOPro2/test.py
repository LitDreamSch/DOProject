import urllib.request
url = 'https://m.zhongziso.com/list/DASD-118/1'
HeaderDict = {# 编好的头消息，防止和谐爬虫
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive'
}
res = urllib.request.Request(url,headers = HeaderDict)
res = urllib.request.urlopen(res)
with open("1.html","w") as f:
    f.write(res.read().decode("utf-8"))
