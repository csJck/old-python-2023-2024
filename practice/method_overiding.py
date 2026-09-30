class human:
    def __init__(self,name):
        self.name = name

    def coding(self):
        print(f"{self.name} the human is coding")


class man(human):
    def __init__(self,name):
        self.name = name

    def coding(self):
        print(f"{self.name} the man is coding")

human = human("john")
man = man("jack")

man.coding()
human.coding()