i=0

def hanni(n, x, y, z):
    
    if n == 1:
        print(x,'->', z)

    else:
        hanni(n-1 ,x ,z ,y)
        print(x, '->', z)
        hanni(n-1, y, x, z)
    i += 1

n = int(input('输入汉诺塔的层数： '))

hanni(n, 'a', 'b', 'c')
print(i)
    
