class Resturant:
    def __init__(self,menu,location,rating):
        self.menu=menu
        self.location=location
        self.rating=rating
    def show(self):
        return {"Menu":self.menu,"Location":self.location,"Rating":self.rating}
    
class Delivery:
    def __init__(self,fee,time):
     self.fee=fee
     self.time=time
    def show(self):
       return {"Fee":self.fee,"Time":self.time}
   
class online(Resturant,Delivery):
    def __init__(self, menu, location, rating,fee,time):
       Resturant.__init__(self,menu, location, rating)
       Delivery.__init__(self,fee,time)
    def show(self):
        return {"Menu":self.menu,"Location":self.location,"Rating":self.rating,"Fee":self.fee,"Time":self.time}
    
s1=online("[daal,roti,baryani]","lahore",5,200,20)

print(s1.show())
s2=Resturant("[daal,roti,baryani]","lahore",5)
print(s2.show())