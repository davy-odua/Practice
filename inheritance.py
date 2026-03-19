#inheritance = Where a class inherits attributes and methods of another class.
#             Example - A child class inherits from a parent class

class Animals:
    def __init__(self, color, name, is_alive):
        self.color = color
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"The {self.color} {self.name} is eating. It is {self.is_alive} ")

    def sleep(self):
        print(f"The {self.name} is sleeping")


class Cat(Animals):
    pass

class Dog(Animals):
    pass

class Mouse(Animals):
    pass

cat = Cat("White", "Pus", True)
dog = Dog("Black", "Bosco", True)
mouse = Mouse("White", "Jerry", True)

cat.eat()
cat.sleep()
dog.eat()
dog.sleep()










