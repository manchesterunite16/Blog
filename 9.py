

def JudgeNum(*parameter):
    
    length = len(parameter)
    
    for i in range(length):
        letter = 0
        number = 0
        space = 0
        other = 0



        for each in parameter[i]:

            if  each.isalpha():

                letter += 1;
            
            elif  each.isdigit():

                number += 1;

            elif  ' ' == each:

                space += 1;

            else:

                other += 1;
        print( '第%d个字符串共有：字符%d个，数字%d个，空格%d个，其他符号%d个。'% (i+1, letter, number, space, other))
            
        
