

import os

vediolist = []

def searchfile(startdir, target)

    os.chdir(startdir)
    
    for eachfile in os.listdir(os.curdir):

        if os.path.splitext(eachfile)[1] in target:

            vediolist.append(os.getcwd() + os.sep +　eachfile)

        if os.path.isdir(eachfile):

            searchfile(eachfile, target)

            os.chdir(os.pardir)


startdir = input('请输入搜索目录：')

target = ['mp4', 'rmvb', 'avi']

seachfile(startdir, target)

f = open(os.getcwd() + os.sep + 'vediolist.txt', 'w')

f.writline(vediolist)

f.close()
