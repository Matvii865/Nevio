import random
class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 100

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        print(f'Skills: {self.skills}')
        print(f'Money: ${self.money}')

    def study(self):
        self.skills += 1
        print("Time to study📕📚🤓🧠")

    def chill(self):
        self.skills -= 0.5
        self.money -= 50
        print("Chilling ...😎😁😊")

    def work(self):
        self.skills += 0.5
        self.money += 50
        print("Hard working ...🤔🤔🤔")


Sasha = Student('Sasha', 12)
#Ivan = Student('Ivan', 6)

Sasha.info()
#Ivan.info()

for day in range(365):
    Sasha.choice = random.randint(1, 3)

    if Sasha.choice == 1:
        Sasha.chill()
    elif Sasha.choice == 2:
        Sasha.work()
    else:
        Sasha.study()

Sasha.age +=1
Sasha.info()
