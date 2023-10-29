class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"
    
blueCar = Car("blue", 20000)
redCar = Car("red", 30000)
for car in (blueCar, redCar):
    print(car)