from urllib import parse,request
from http import cookiejar
import gzip
import re
import os
import time
import msvcrt


cj = cookiejar.MozillaCookieJar("cookies.txt")  #创建与Mozilla浏览器cookies.txt兼容的FileCookieJar实例
opener  = request.build_opener(request.HTTPCookieProcessor(cj)) #创建opener对象，自动处理cookies
   

DefaultHeaders = {
            "Accept":"*/*",
            "User-Agent":"Symbian",
            "Accept-Language":"zh-cn",
            "Accept-Encoding":"gzip;deflate",
            "Connection":"keep-alive",
            "Referer":"http://m.baidu.com/"
}

#密码输入，cmd命令行下运行显示*号
def pwd_input():  
    chars = [] 
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("【温馨提醒：当前未在cmd命令行下运行，密码输入无法隐藏】:\n")
        if newChar in "\r\n":            
             break 
        elif newChar == "\b":
             if chars:  
                 del chars[-1] 
                 msvcrt.putch("\b".encode(encoding="utf-8"))
                 msvcrt.putch( " ".encode(encoding="utf-8"))
                 msvcrt.putch("\b".encode(encoding="utf-8"))                 
        else:
            chars.append(newChar)
            msvcrt.putch("*".encode(encoding="utf-8"))
    return ("".join(chars) )


def Http(url,charset="utf-8",headers=DefaultHeaders):
    rr = request.Request(url=url, headers=headers)
    with opener.open(rr) as fp:
        if fp.info().get("Content-Encoding") == 'gzip':
            f = gzip.decompress(fp.read())
            res = f.decode(charset)
        else:
            res = fp.read().decode(charset)
    return res

#POST访问
def Post(url,postdata,charset="utf-8",headers=DefaultHeaders):
    if postdata:
        postdata = parse.urlencode(postdata).encode("utf-8")
    rr = request.Request(url=url,headers=headers,data=postdata)
    with opener.open(rr) as fp:
        if fp.info().get("Content-Encoding") == "gzip":
            f = gzip.decompress(fp.read())
            res = f.decode(charset)
        else:
            res = fp.read().decode(charset)
    return res

class baidu:
        #验证码处理
    def GetVerifyCode(self,vcodestr):
        img = "http://wappass.baidu.com/cgi-bin/genimage?%s"%vcodestr
        with open("verify.jpg","wb") as f:
            f.write(request.urlopen(img).read())
        os.popen("verify.jpg")
        verify = input("\n需要输入验证码，请输入打开的图片\"verify.png\"中的验证码：\n").strip()
        return verify

    def login1(self,bdcm,uid):
        postdata = {
                    'bdcm' : bdcm,
                    'bd_page_type' : '1',
                    'from' : '',
                    'isphone' : '0',
                    'password' : self.password ,
                    'pu' : 'sz@224_220,',
                    'ssid' : '',
                    'submit' : '%E7%99%BB%E5%BD%95',
                    'tn' : 'bdIndex',
                    'tpl' : 'tb',
                    'type' : '',
                    'u' : 'http%3A%2F%2Ftieba.baidu.com/?mo_device=1',
                    'uid' : uid,
                    'username' : self.username,
                    'vcodestr' : '',
                    }
        res = Post("http://wappass.baidu.com/passport/login",postdata)
        match = re.search('un=(.*?)">',res)
        if match:
            print("\n【"+parse.unquote(match.group(1))+"】：登录成功")
            global checklogin
            checklogin = True 
            if cj:
                cj.save(ignore_discard = True, ignore_expires = True)
        elif res.find("请您输入验证码") != -1:
            print("请您输入验证码！\n")
            match = re.search('name="vcodestr" value="(.*?)"/>',res)
            if match:
                vcodestr = match.group(1)
                VerifyCode = self.GetVerifyCode(vcodestr)
                self.login2(uid,vcodestr,VerifyCode)
        elif res.find("您输入的验证码有误") != -1:
            print("您输入的验证码有误！\n")
            match = re.search('name="vcodestr" value="(.*?)"/>',res)
            if match:
                vcodestr = match.group(1)
                VerifyCode = self.GetVerifyCode(vcodestr)
                self.login2(uid,vcodestr,VerifyCode)
        elif res.find("您输入的密码有误") != -1:
            print("您输入的密码有误！\n")
            self.getstr()
        elif res.find("用户名格式错误") != -1:
            print("用户名格式错误！\n")
            self.getstr()
        elif res.find("您的帐号不存在") != -1:
            print("您的帐号不存在！\n")
            self.getstr()
        else:
            self.getstr()
                

    def login2(self,uid,vcodestr,VerifyCode):        
        postdata = {
                    'bdcm' : '',
                    'bd_page_type' : '1',
                    'from' : '',
                    'isphone' : '0',
                    'password' : self.password ,
                    'pu' : 'sz@224_220,',
                    'ssid' : '',
                    'submit' : '%E7%99%BB%E5%BD%95',
                    'tn' : 'bdIndex',
                    'tpl' : 'tb',
                    'type' : '',
                    'u' : 'http%3A%2F%2Ftieba.baidu.com/?mo_device=1',
                    'uid' : uid,
                    'username' : self.username,
                    'vcodestr' : vcodestr,
                    'verifycode' : VerifyCode,
                    }
        res = Post("http://wappass.baidu.com/passport/login",postdata)
        match = re.search('un=(.*?)">',res)
        if match:
            print("\n【"+parse.unquote(match.group(1))+"】：登录成功")
            global checklogin
            checklogin = True
            if cj:
                cj.save(ignore_discard = True, ignore_expires = True)
        elif res.find("请您输入验证码") != -1:
            print("请您输入验证码！\n")
            match = re.search('name="vcodestr" value="(.*?)"/>',res)
            if match:
                vcodestr = match.group(1)
                VerifyCode = self.GetVerifyCode(vcodestr)
                self.login2(uid,vcodestr,VerifyCode)
        elif res.find("您输入的验证码有误") != -1:
            print("您输入的验证码有误！\n")
            match = re.search('name="vcodestr" value="(.*?)"/>',res)
            if match:
                vcodestr = match.group(1)
                VerifyCode = self.GetVerifyCode(vcodestr)
                self.login2(uid,vcodestr,VerifyCode)
        elif res.find("您输入的密码有误") != -1:
            print("您输入的密码有误！\n")
            self.getstr()
        elif res.find("用户名格式错误") != -1:
            print("用户名格式错误！\n")
            self.getstr()
        elif res.find("您的帐号不存在") != -1:
            print("您的帐号不存在！\n")
            self.getstr()
        else:
            self.getstr()

        
    def getstr(self):
        self.username = input("请输入百度账号:\n").strip()
        print("请输入账号密码:")
        self.password = pwd_input().strip()
        res = Http("http://wappass.baidu.com/passport/?login&u=http%3A%2F%2Ftieba.baidu.com/?mo_device=1")
        match = re.search('name="uid" value="(.*?)"/>',res)
        if match:
            self.uid = match.group(1)
        match = re.search('name="bdcm" value="(.*?)"/>',res)
        if match:
            self.bdcm = match.group(1)
            self.login1(self.bdcm,self.uid)

    def __init__(self):
        if os.path.exists("cookies.txt"):
            try:
                cj.load()
                if cj:
                    print("导入cookies.txt成功，正在尝试自动登录……\n")
                    res = Http("http://tieba.baidu.com/?mo_device=1")
                    match = re.search('un=(.*?)">',res)
                    if match:
                        print("\n【"+parse.unquote(match.group(1))+"】：登录成功")
                        global checklogin
                        checklogin = True               
                        if cj:
                            cj.save(ignore_discard = True, ignore_expires = True)
                    else:
                        self.getstr()
            except:
                print("cookies格式错误，开始手动登录……\n")
                self.getstr()
        else:
            print("未发现cookies.txt文件，开始手动登录……\n")
            self.getstr()
     



if __name__ == "__main__":
    print("【百度贴吧签到机 By:comeheres【http://www.8zata.com】")
    print("正在检测是否可以自动登录……")
    baidu()


if checklogin == True:
    print("\n贴吧详情：")
    listaddr = []
    i = 1
    res = Http("http://tieba.baidu.com/mo/m?tn=bdFBW&tab=favorite")
    for match in re.findall('\.<a href="(.*?)">(.*?)</a></td><td align="center">(.*?)</td><td align="center">(.*?)</td>',res):
        listaddr.append([match[0],match[1]])
        print(str(i)+"."+match[1]+"——"+match[2]+"——"+match[3])
        i+=1
    if len(listaddr) != 0:
        print("\n开始签到：")
        for j in range(0, len(listaddr)):
            url = "http://tieba.baidu.com"+listaddr[j][0]
            res = Http(url)
            if res.find(">已签到<") != -1:
                print(str(j+1)+".【"+listaddr[j][1]+"】：已签到！")
            elif res.find(">签到<") != -1:
                match = re.search('等级(.*?)\)</td><td style="text-align:right;"><a href="(.*?)">签到',res)
                if match:
                    url =  ("http://tieba.baidu.com"+match.group(2)).replace('&amp;','&')
                    res = Http(url)
                    if res.find("签到成功") != -1:
                        match = re.search('签到成功，经验值上升<span class="light">(.*?)<',res)
                        if match:
                            print(str(j+1)+".【"+listaddr[j][1]+"】：签到成功，经验值上升"+match.group(1))
    else:
        print("你还没加入任何一个贴吧！")

print("3秒后，自动关闭")
time.sleep(1)
print("2秒后，自动关闭")
time.sleep(1)
print("1秒后，自动关闭")
time.sleep(1)
exec("quit()")
