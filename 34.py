def power_1(x, y):
    return (x ** y)

def power_2(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

import time
start = time.clock()
power_1(144764326432, 100)
time_1 = time.clock()
power_2(144764326432, 100)
time_2 = time.clock()
print("power_1运行了{0}秒".format(time_1 - start))
print("power_2运行了{0}秒".format(time_2 - time_1))
