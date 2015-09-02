

class Ticket:

    def __init__(self, weekend = False, child = False):

        self.ticket = 100

        if weekend:
            self.time = 1.2
        else:
            self.time = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def price(self, num):

        return self.ticket * self.time * self.discount * num

adult = Ticket()
child = Ticket(child = True)

print('2个大人和1个孩子平时的票价共：',str((adult.price(2) + child.price(1))))


