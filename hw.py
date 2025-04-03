from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class BMW(Vehicle):
    def start_engine(self):
        return "BMW engine started with a roar!"

    def stop_engine(self):
        return "BMW engine stopped smoothly."

class Ferrari(Vehicle):
    def start_engine(self):
        return "Ferrari engine started with a powerful vroom!"

    def stop_engine(self):
        return "Ferrari engine stopped with a purr."

def test_vehicle(vehicle):
    print(vehicle.start_engine())
    print(vehicle.stop_engine())

# Creating instances of BMW and Ferrari
bmw = BMW()
ferrari = Ferrari()

# Testing the vehicles
test_vehicle(bmw)
test_vehicle(ferrari)
