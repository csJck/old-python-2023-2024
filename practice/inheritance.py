class Vehicle:
    moves = True
    turns = True

    def drive(self):
        print(f"this {self.name} is driving")

    def stop(self):
        print(f"This {self.name} has stopped.")


class Car(Vehicle):
    wheels = 4

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Motorbike(Vehicle):
    wheels = 2

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


bike1 = Motorbike("Bikey","Suzuki")

Car1 = Car("GTR", "Nissan")

Car1.drive()

bike1.stop()

print(Car1.moves)
print(bike1.turns)
