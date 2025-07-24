# class Car:
#     def __init__(self,fule_type):
#         self.fule_type=fule_type
#     def type(self):
#         print("tpye:",self.fule_type)

# class ElectricCar(Car):
#     def __init__(self,fule_type):
#         super().__init__(fule_type)
#     def type2(self):
#         self.type()
    
# s1=ElectricCar("eneryg")
# s1.type()
# s1.type2()

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print("Name; ",self.name)

# class Student(Person):
#     def __init__(self, name,age,rollnumber):
#         super().__init__(name)
#         self.age=age
#         self.rollnumber=rollnumber
#     def detail(self):
#         self.show()
#         print("Age: ",self.age)
#         print("Rollnumber: ",self.rollnumber)

# s1=Student("ali",21,45678)
# s1.detail()
# s1.show()

class shape:
    def area():
        return 0
    
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def show(self):
        print("area is ",self.width*self.height)

s=Rectangle(4,5)
print(s.show())
        
