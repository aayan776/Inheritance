class dad:
    def __init__(self, eyes, height):
        self.eye = eyes
        self.height = height
    def display(self):
        print(f"The color of your eyes is {self.eye}. You are also {self.height} meters in length.")
class son(dad):
    def __init__(self, name, age, eyes, height):
        self.name = name
        self.age = age
        dad.__init__(self, eyes, height)
child = son("Tawseef", 14, "Black", 1.8)
child.display()

class Vehicle:
    def __init__(self, name, max, mileage):
        self.model = name
        self.speed = max
        self.mileage = mileage
class Bus(Vehicle):
    pass
school_bus = Bus("School Bus", 80, 1284)
print(f"The model is: {school_bus.model}. The max speed is: {school_bus.speed}. The mileage is: {school_bus.mileage}")

class Bird:
    def __init__(self):
        print("Bird is ready.")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster.")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin ready.")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster.")
pengu = Penguin()
pengu.whoisthis()
pengu.swim()
pengu.run()