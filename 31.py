import time as t

class MyTimer():
    #将所有对象定义,python 中没有声明，只有定义
    def __init__(self):
        self.unit = ['年', '月', '天', '时', '分', '秒']
        self.prompt = '未开时计时'
        self.lasted = 0
        self.begin = 0
        self.end = 0
    # 重写__str__ 和 __repr__方法是为可能够值输入t1时就能输出结果    
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    #计算总时间
    def __add__(self, other):
         prompt = '总共运行了'
         result = []
         for index in range(6):
             result.append(self.lasted[index] + other.lasted[index])
             if result[index]:
                 prompt += (str(result[index]) + self.unit[index])
         return prompt
        
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '请先调用stop()停止计时！'
        print('开始计时。。。。')

    #结束计时
    def stop(self):
        if not self.begin:
            print('请先调用start()开始计时！')
        else:
            self.end = t.localtime()
            self.calc()
            print('计时结束！')

    # 计算运行时间
    def calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        
        # 下一轮计时，要初始化
        self.begin = 0
        self.end = 0
