class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed 
        self.mileage=mileage
modelX=Vehicle(240,18)
print("m:",modelX.max_speed)
print("m:",modelX.mileage)