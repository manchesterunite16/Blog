class C2F(float):
        "摄氏度转换为华氏度"
        def __new__(cls, arg=0.0):
                return float.__new__(cls, arg * 1.8 + 32)


temperature = int(input('请输入摄氏温度： '))
a = C2F(temperature)

print(a)
