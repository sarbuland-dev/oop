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

# class shape:
#     def area():
#         return 0
    
# class Rectangle(shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def show(self):
#         print("area is ",self.width*self.height)

# s=Rectangle(4,5)
# print(s.show())
        
# class person:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print("name",self.name)

# class teacher(person):
#     def __init__(self,name,department):
#         super().__init__(name)
#         self.department=department
#     def show(self):
#       super().show()
#       print("department",self.department)

# class studentb(teacher):
#     def __init__(self,name,department,id):
#         super().__init__(name,department)
#         self.id=id
#     def show(self):
#         super().show()
#         print("id",self.id)


# s1=studentb("ali","soft",123345)
# s1.show()


# class sportcar:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     def details(self):
#         print("name",self.name)
#         print("model",self.model)

# class SUV(sportcar):
#     def __init__(self,name,model,speed):
#         super().__init__(name,model)
#         self.speed=speed
#     def details(self):
#         super().details()
#         print("speed",self.speed)

# class Electriccar(SUV):
#     def __init__(self, name, model, speed,battery):
#         super().__init__(name, model, speed)
#         self.battery=battery
#     def details(self):
#          super().details()
#          print("battery",self.battery)

# s1=SUV("tesla","aun4567",230,)
# s1.details()

class shape:
    def area(self):
         return 0
        

class circle(shape):
     def __init__(self,radius):
          self.raduis=radius
     def area(self):
         return 3.14*self.raduis*self.raduis
     
class rectangle(circle):
     def __init__(self,lenght,height):
          self.lenght=lenght
          self.height=height
     def area(self):
         return self.height*self.lenght
     
s1=rectangle(24,56)
print(s1.area())
s2=circle(34)
print(s2.area())


    


        

        

    
