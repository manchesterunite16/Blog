
import random as r
len_x = [0, 10]
len_y = [0, 10]

class Turtle:
   
    def __init__(self):
       self.power = 100
       self.x = r.randint(len_x[0] , len_x[1])
       self.y = r.randint(len_y[0], len_y[1])

    def move(self):

        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])

        if new_x > len_x[1]:

            self.x = len_x[1] - (new_x - len_x[1])
        elif new_x < len_x[0]:
            self.x = len_x[0]- (new_x - len_x[0])

        else:
            self.x = new_x

        if new_y > len_y[1]:

            self.y = len_y[1] - (new_y - len_y[1])
        elif new_y < 0:
            self.y = len_y[0] - (new_y - len_y[0])

        else:
            self.y = new_y

        
            
        self.power -= 1

        return (self.x, self.y)
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
   
    def __init__(self):
        
       self.x = r.randint(len_x[0], len_x[1])
       self.y = r.randint(len_y[0], len_y[1])

    def move(self):

        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])

        if new_x > len_x[1]:

            self.x = len_x[1] - (new_x - len_x[1])
        elif new_x < len_x[0]:
            self.x = len_x[0]- (new_x - len_x[0])

        else:
            self.x = new_x

        if new_y > len_y[1]:

            self.y = len_y[1] - (new_y - len_y[1])
        elif new_y < 0:
            self.y = len_y[0] - (new_y - len_y[0])

        else:
            self.y = new_y
        return (self.x, self.y)
    

turtle = Turtle()
fish = []

for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:

    if not len(fish):
        print("鱼儿被吃光了！")
        break
    if not turtle.power:
        print("乌龟体能耗尽！")
        break
    pos = turtle.move()

    for each_fish in fish[:]:

        if each_fish.move() == pos:

            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了！")
      
