class Organism:
    alive = True

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def live(self):
        print(f"{self.name} is living on earth.")

class Animal:
    conscious = True

    def __init__(self,name,type):
        self.name = name
        self.type = type

class Human(Organism,Animal):
    intelligent = True

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


human1 = Human("jack","male")

human1.live()

print(human1.alive)
print(human1.conscious)