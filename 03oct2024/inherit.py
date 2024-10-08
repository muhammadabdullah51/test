class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def food(self):
        return f"the food of {self.name} is petrol"
class Person:    
    def __init__(self, name):
        self.name = name
    def food(self):
        return f"the food of {self.name} is pasta"
class Animal:
    def __init__(self, name):
        self.name = name
    def food(self):
        return f"the food of {self.name} is grass"

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(self.name)


# vhl = Vehicle('car')
# per = Person('abdullah')
# anm = Animal('penguine')

# print(vhl.food())
# print(per.food())
# print(anm.food())