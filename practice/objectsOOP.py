class Pro:
    game = "Fortnite"

    def __init__(self,name,region,inputd):
        self.name = name
        self.region = region
        self.inputd = inputd

    def play(self):
        print(self.name, "is playing fortnite.")

    def relaxing(self):
        print(self.name, "is relaxing.")


pro1 = Pro("Mongraal","Europe","Keyboard")
pro2 = Pro("MrSavage","Europe","Keyboard")
pro3 = Pro("Mero", "North America", "Controller")
pro4 = Pro("MoneyMaker","Europe","Controller")

print(pro1.name)
print(pro2.region)
print(pro3.inputd)

pro1.play()
pro1.relaxing()




















