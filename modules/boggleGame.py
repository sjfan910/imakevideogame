class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog('buddy', 3)
dog2 = Dog('lucy', 4)

dog1.bark()