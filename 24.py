

import pickle


def savefile(boy, girl, count):
    
    boyfilename = 'boy' + str(count) + '.txt'
    girlfilename = 'girl' + str(count) + '.txt'

    boyfile = open(boyfilename, 'wb')
    girlfile = open(girlfilename, 'wb')

    #boyfile.writelines(boy)
    #girlfile.writelines(girl)

    pickle.dump(boy, boyfile)
    pickle.dump(girl, girlfile)

    boyfile.close()
    girlfile.close()
    
def splitfile(filedir):
    f = open('C:\\Users\\Parhatjan\\Desktop\\record.txt')

    boy = []
    girl = []
    count = 1

    for eachline in f:
        if eachline[:8] != '========':
            (role, lineword) = eachline.split(':', 1)
            if role == '小甲鱼':
                boy.append(lineword)
            if role == '小客服':
                girl.append(lineword)

        else :
            savefile(boy, girl, count)

            boy = []
            girl = []
            count += 1
            
    savefile(boy, girl, count)

    f.close()
            

splitfile('C:\\Users\\Parhatjan\\Desktop\\record.txt')        
    
