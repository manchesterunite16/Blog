

count = 3
keys = '000'
while count:
    key = input('请输入密码：')
    if keys == key:
        print('密码正确')
        break
    elif '*' in key:
        list1 = list(key)
        list1.remove('*')
        print(list1)
        print('程序中不能有*')
        continue
    else:
        print('密码错误')
        
    count -= 1
