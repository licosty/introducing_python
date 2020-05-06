''' Страница упражнения - 178 '''

# 1
class Thing():
    pass

print(Thing)
example = Thing()
print(example)

# 2
class Thing2():
    letters = 'abc'

print(f"\n{Thing2.letters}")

# 3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

print(f"\n{Thing3().letters}")

# 4
class Element():
    def __init__(self, name, symbol, number):
        # self.name = name
        # self.symbol = symbol
        # self.number = number

        # 8
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    # 6
    def dump(self):
        print(self.__name, self.__symbol, self.__number)

    # 7
    def __str__(self):
        return f"{self.__name} {self.__symbol} {self.__number}"

    # 8
    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

element = Element('Hydrogen', 'H', 1)

# 5
elements = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**elements)

# 6
print()
element.dump()

# 7
print(f"\n{hydrogen}")

# 8
print()
print(element.name)
print(element.symbol)
print(element.number)

# 9
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

print()
bear = Bear()
rabbit = Rabbit()
oct = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(oct.eats())

# 10
class Laser():
    def does(self):
        return 'desintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, laser, claw, smart_phone):
        self.laser = laser
        self.claw = claw
        self.smart_phone = smart_phone

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smart_phone)