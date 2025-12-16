import math
class Car:
    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed

    def distance(self):
        distance = self.tank_capacity / self.fuel_consumption * 100
        return distance


class Truck(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, weight):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.weight = weight

    def ratio(self):
        fuel_for_250 = self.fuel_consumption * 2.5
        ratio = math.floor(self.weight / fuel_for_250)
        return ratio


class Bus(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, kids, adults):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.kids = kids
        self.adults = adults

    def ratio(self):
        total_weight = self.kids * 35 + self.adults * 70
        fuel_for_250 = self.fuel_consumption * 2.5
        ratio = math.floor(total_weight / fuel_for_250)
        return ratio


if __name__ == "__main__":
    truck = Truck(200, 25, 80, 5000)
    bus = Bus(300, 30, 60, 10, 20)

    print("Грузовик:")
    print(f"Максимальная дистанция: {truck.distance()} км")
    print(f"Соотношение: {truck.ratio()}")
    print('-----------------------')
    print("Автобус:")
    print(f"Максимальная дистанция: {bus.distance()} км")
    print("Соотношение:", bus.ratio())
