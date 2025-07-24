# class Student:
#     def __init__(self,name,age,rollnumber):
#         self.name=name
#         self.age=age
#         self.rollnumber=rollnumber
#     def details(self):
#         print("Name: ",self.name)
#         print("age: ",self.age)
#         print("rollnumber: ",self.rollnumber)

# s1=Student("Ali",21,34)
# s2=Student("Ahmad",18,12)
# s3=Student("ali ahmad",21,34)
# (s1.details())
# (s2.details())
# (s3.details())
#   2 question
# class Car:
#     def __init__(self,brand,model,car_number):
#         self.brand=brand
#         self.model=model
#         self.car_number=car_number
#     def details(self):
#         print("Brand; ",self.brand)
#         print("model; ",self.model)
#         print("car_number; ",self.car_number)
        
# car1=Car("tata",2023,"Ajk 4540")
# car1.details()
# print('____________________________')
# car2=Car("tesla",2023,"Ajk 4540")
# car2.details()
# print('____________________________')
# car3=Car("lamo",2023,"Ajk 4540")
# car3.details()
# 3 question

class Animal:
    def __init__(self,name):
        self.name=name
    def details(self):
        if self.name=="Dog":
            return "bark"
        elif self.name=="Cat":
            return "mewo"
        else:
            return("not correct")
        
dog=Animal("Dog")
print(dog.details())
cat=Animal("er")
print(cat.details())

        


        