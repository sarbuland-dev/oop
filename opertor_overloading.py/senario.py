class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__ (self,other):
        return Vector(self.x+other.x,self.y+ other.y)
    def __str__(self):
        return (f"{self.x},{self.y}")
    
p1=Vector(4,2)
p2=Vector(2,2)
print(p1+p2)

        
        