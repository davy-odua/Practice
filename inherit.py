
class GrandFather:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print(f"{self.name} is eating at the moment. {self.name} is {self.age} years old")

class GrandMother:                #from mother side
    def __init__(self, name, age):
        self.name =name
        self.age = age

class Father(GrandFather):
    pass

class Mother(GrandMother):
    pass

class Boy(Father, Mother):
    pass

class Girl(Father, Mother):
    pass

boy = Boy("Mathew", 16)
girl = Girl("Caroline", 15)
father = Father("John", 40)
mother = Mother("Mercy", 35)
grandfather = GrandFather("James", 60)
#Attributes
print(f"This boy is called {boy.name} and is {boy.age} years old ")
print(f"This girl is called {girl.name} and is {boy.age} years old ")
print(f"His father is called {father.name} and is {boy.age} years old ")
print(f"Her mother is called {mother.name} and is {boy.age} years old ")
print(f"Their grandfather is called {grandfather.name} and is {boy.age} years old ")

print("")
#Methods(functions)
boy.eating()
grandfather.eating()





