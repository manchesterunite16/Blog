def funX():
    x = 5
    def funY():
        #nonlocal x
        y = x
        return x
    return funY

a = funX()
#print(a())
#print(a())
#print(a())
