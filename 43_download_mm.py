import urllib.request
import os
import re

def url_open(url):
    
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    
    html = url_open(url).decode('utf-8')
    a = re.findall(r'<span class="current-comment-page">[[0-9]+]</span>',html)
    b = re.findall(r'[0-9]+', a[0])
    c = int(b[0])
    return c
    
def find_image(url):
    
    html = url_open(url).decode('utf-8')
    
    img_addrs = []
    p = r'<img src="([^"]+\.jpg)"'
    img_addrs = re.findall(p, html)
    print(img_addrs)
    
    return img_addrs     

def save_imgs(folder, img_addrs):
    
    for each in img_addrs:
        filename = each.split('/')[-1]  # 最后一个名字
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)
               
def download_mm(folder = 'XXOO', pages=20):
    os.mkdir(folder)         # 创建文件夹用来保存文件
    os.chdir(folder)         # 改变目录地址，使之为当期目录

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_image(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
        
