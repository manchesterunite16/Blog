class timeslong(object):
    def __init__(self,func):
        self.f = func
    def __call__(self):
        start = time.clock()
        print("It's time starting ! ")
        self.f()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)

    @timeslong
    def f():
        y = 0
        for i in range(10):
            y = y + i + 1
            print(y)
        return y

    print(f())
