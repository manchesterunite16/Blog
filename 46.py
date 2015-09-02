
class dictclass(object):

    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def del_dict(self, key):
        self.dict1.pop(key)
        print(self.dict1)

    def get_dict(self, key):
        if self.dict1.get(key):
            print(self.dict1.get(key))
        else :
            print('not found')
        
    def get_key(self):
        l = list(self.dict1.keys())
        print(l)

    def update_dict(self):
        self.dict1.update(self.dict2)
        val = list(self.dict1.values())
        print(val)

dict1 = {1:'1', 2:'2', 3:'3'}
dict2 = {3:'6', 4:'8'}

d = dictclass(dict1, dict2)
i = int(input('请输入要删除的键值：'))
try:
    d.del_dict(i)
except KeyError:
    print('你输入有误')
    
j = int(input('请输入要判断的键值：'))
d.get_dict(j)


        




    
    
