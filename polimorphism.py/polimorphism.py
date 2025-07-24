class Car:
    def start(self): print("Car started")

class Bike:
    def start(self): print("Bike started")

for vehicle in [Car(), Bike()]:
    vehicle.start()
