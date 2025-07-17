import random
class Student:
    educational_platform = 'udemy'
    def __init__(self, name, age=34):
        self.name = name
        self.age = age
    def greet(self):
        greetings = ["Hi, I'm ", "Hey, there, my name is ", "Hi. Oh, my name is "]
        index = random.randrange(0, 2, 1)
        greeting = f"{greetings[index]}{self.name}"
        return greeting

s1 = Student('Andrew', age=23)
print(s1.greet())