class primate:

    bipedal = True
    fingers = 10

    def __init__(self,name):
        self.name = name

    def hunt(self):
        print(f"the {self.name} is hunting.")


class human(primate):

    intelligent = True

    def __init__(self,name):
        self.name = name

    def learn(self):
        print(f"{self.name} is learning")

class male(human):

    has_penis = True

    def __init__(self,name):
        self.name = name


primate = primate("ape")
human = human("charlie")
male = male("Jack")

male.learn()
primate.hunt()

print(male.bipedal)
print(male.has_penis)