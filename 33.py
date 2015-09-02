class Centigrade:
    def __init__(self, value = 25.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return float(instance.cen * 1.8 + 32)

    def __set__(self, instance, value):
        instance.cen = (float(value) - 32) / 1.8

class Temperature:
    cen = Centigrade()
    fah = Fahrenheit()
