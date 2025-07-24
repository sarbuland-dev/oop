class Vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehical):
    pass
    def move(self):
     return ("move")

class plane(Vehical):
    pass
    def move(self):
     return ("fly")

car1=Car("tesla",2025)
plane1=plane("PIA",2013)
for x in (car1,plane1):
    print(x.brand)
    print(x.model)
    print(x.move())


        