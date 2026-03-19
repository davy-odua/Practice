#Multiple inheritance = Where a child class inherits from more than one parent classes
#                       C(A, B)

#Multilevel inheritance = Where a class inherits from a parent class which also inherits from another parent class. Example, child, parent and grandparent relationship
#Example                 C(B) <- B(A) <- A

class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):

    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bosco", True)
hawk = Hawk("Lave", True)
fish = Fish("Fillet", False)

fish.eat()






