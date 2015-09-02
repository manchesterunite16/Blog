#欺骗服务器 ,隐藏header
import urllib.request
import urllib.parse
import json
import time

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
while(1):
    content = input('请输入需要翻译的内容：')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=fanyi.logo'
    date = {}
    date['type'] = 'AUTO'
    date['i'] = content
    date['doctype'] = 'json'
    date['xmlVersion'] = '1.6'
    date['keyfrom'] ='fanyi.web'
    date['ue'] = 'UTF-8'
    date['typoResult'] = 'true'
    
    date = urllib.parse.urlencode(date).encode('utf-8')

    req = urllib.request.Request(url, date, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('翻译结果为： %s' % (target['translateResult'][0][0]['tgt']) )

    time.sleep(5)
