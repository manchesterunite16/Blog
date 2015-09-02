

import os

def searchfile(startdir, targetfile)

    os.chdir(startdir)

    for eachfile in os.listdir(os.curdir)

        if eachfile == target:

            print(os.gercwd() + os.sep + eachfile)

        if os.path.isdir(eachfile):

                searchfile(eachfile, target)

                os.chdir(os.pardir)

startfile = input('请输入搜索路径：')

target = input('请输入目标文件：')

searchfile(startfile, target)
