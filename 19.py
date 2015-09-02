

import os

allfile = os.listdir(os.curdir)
typedict = dict()

for eachfile in allfile:
    if os.path.isdir(eachfile):   #判断当前目录中是否有文件夹

        typedict.setdefault('文件夹',  0)   #有的话，将文件夹添加到字典中去，其中key为‘文件夹’,值为0
        typedict['文件夹'] += 1

    else:

        ext = os.path.splitext(eachfile)[1]
        typedict.setdefault(ext, 0)
        typedict[ext] += 1

for eachtype in typedict.keys():
    
    print('当前目录下共有类型为【%s】的文件%d 个' %  (eachtype, typedict[eachtype]))
    
