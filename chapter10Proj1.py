class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

# Create a Car object
car = Car(2024, "Example Make")

# Call accelerate method five times and display current speed
for _ in range(5):
    car.accelerate()
    print(car.get_speed())

# Call brake method five times and display current speed
for _ in range(5):
    car.brake()
    print(car.get_speed())
