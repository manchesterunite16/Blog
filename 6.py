count = 3
keys = '000'
while count:
    key = print('请输入密码：')
    if key == keys:
        print('密码正确')
        break
    elif '*' in key:
        print('程序中不能有*')
        continue
    else:
        print('密码错误')
        
    count -= 1
