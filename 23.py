

import os

# 找出所有txt文件，并在目标文件中找出key的位置，并打印出来

def searchfile(key):                              
    
    allfile = os.walk(os.getcwd())                                           # 遍历所有文件，返回一个三元元组

    txtfile = []                                                             # 用于存放所有txt文件
    
    for t in allfile:                                                        # 对于所有的元组t

        for eachfile in t[2]:                                                # 元组t[2]是一个存放文件

            if os.path.splitext(eachfile)[1] = 'txt':            

                eachfiledir = os.path.join(t[0],eachfile)                    # 将所有txt文件和目录拼接 ，参照os.walk(path)的返回值形式

                txtfile.append(eachfiledir)                                   

        for eachtxtfile in txtfile:

            dictkeyfile = searchinfile(eachtxtfile, key)                     # 调用searchinfile,对每一个txt文件进行查找，返回值为存放key位置的字典

        if dictkeyfile:

            print('在文件加 %s 下发现含关键字： %s' % (eachfile, key))        #将key 的位置打印出来

            printpos(dictkeyfile)
            

# 在目标文件中查找关键字        

def searchinfile(targetfile, key):

    f = open(targetfile)                                                    

    dictkey = dict()                                                        # 建立一个空字典，用于存放key的行数和位置

    count = 0                                                               # 用于标记行数
    
    for eachline in f:

        count += 1
        
        if key in eachline:

            pos = keyinline(eachline, key)                                  # 调用keyinline查找key在这一行中的具体位置 

            dictkey[count] = pos                                            # 将行数和位置写入字典

    return dictkey

    f.close()
    
# 在每一行中查找key的具体位置

def keyinline(line,key):

    begin = line.find(key)                                                  # find(seq, [start,[end) 查找key的最低的索引值，就是第一个索引值

    pos = []                                                                # 定义空列表，用于存放 key的位置
    
    while begin != -1:                    

        pos.append(begin+1)

        begin = line.find(key, begin+1)                                     #从下一个位置继续寻找， 最终返回的是一个存放位置的列表

    return pos

def printpos(dictkeyfile):

    keys = dictkeyfile.keys()                                              # 此时的keys相当于行数，value就是具体的位置

    keys = sorted(keys)                                                    #由于字典是无序的，这里进行一个简单的排序，从小的行数开始打印
    
    for eachkeys in keys:

        print('关键字出现在第%s行，第%s位置' % (eachkeys, str(dictkeyfile[eachkeys])))
    

key = input('输入要搜索的关键字：')

searchfile(key)

    
            

    
