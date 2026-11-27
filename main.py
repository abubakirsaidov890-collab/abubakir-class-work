
class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print(f"Название: {self.name}")
        print(f"Скорость: {self.speed} км/ч")

    def move(self):
        print(f"{self.name} движется со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"{self.name} — {self.speed} км/ч"


class Car(Transport):
    def move(self):
        print(f"{self.name} едет по дороге")


class Bicycle(Transport):
    def move(self):
        print(f"{self.name} едет по велосипедной дорожке")


class Plane(Transport):
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude

    def info(self):
        super().info()
        print(f"Высота: {self.altitude} метров")

    def move(self):
        print(f"{self.name} летит на высоте {self.altitude} метров")


# Задание со звёздочкой
class ElectricCar(Car):
    def __init__(self, name, speed, battery_charge):
        super().__init__(name, speed)
        self.battery_charge = battery_charge

    def move(self):
        super().move()
        print(f"Остаток заряда батареи: {self.battery_charge}%")


# Создание объектов
transport1 = Car("BMW", 220)
transport2 = Bicycle("Scooter", 40)
transport3 = Plane("Boeing", 900, 10000)
transport4 = ElectricCar("Tesla", 250, 85)

# Список транспорта
transports = [
    transport1,
    transport2,
    transport3,
    transport4
]

# Перебор объектов
for transport in transports:
    print("\n--------------------")
    print(transport)
    transport.info()
    transport.move()
