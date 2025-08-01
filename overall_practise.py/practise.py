class book:
    def __init__(self,title,writer,price):
        self.title=title
        self.writer=writer
        self.price=price
    def show(self):
        print("title",self.title)
        print("writer",self.writer)
        print("price",self.price)
    def discount(self,dis_amount):
        
        if dis_amount>0:
            dis_value=(dis_amount/100)*self.price
            final_price=self.price-dis_value
            return final_price

s1=book("the hate","me",1234)
s1.show()
s2=book("the love","me",1234)
s2.show()
s3=book("neutral","me",1234)
s3.show()
print(s1.discount(50))

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"Name is {self.name}")
#         print(f"age is {self.age}")

# class teacher(person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject=subject
#     def show(self):
#         super().show()
#         print("subject",self.subject)

# class student(person):
#     def __init__(self,name,age,subject,rollnumber):
#         super().__init__(name,age)
#         self.subject=subject
#         self.rollnumber=rollnumber
#     def show(self):
#         super().show()
#         print("subject",self.subject)

#         print("rollnumber",self.rollnumber)

# s1=student("ali",21,"math",12321432)
# s1.show()


# class bird:
#     def fly(self):
#         print("bird is amazing")

# class saparrow(bird):
#     def fly(self):
#         print("saparrow can fly")

# class ostrich(bird):
#     def fly(self):
#         print("ostrich cant run")

# s1=[saparrow(),ostrich()]
# for bird in s1:
#     bird.fly()


# class bank:
#     def __init__(self,ower,blance):
#         self.ower=ower
#         self.__blance=blance
#     def deposit(self,amount):
#         if amount>0:
#              self.__blance+=amount 
#         else:
#             print("ivalid")
#     def withdraw(self,amount):
#         if 0<amount<=self.__blance:
#             self.__blance-=amount
#         else:
#             print("invail")
#     def get_blance(self):
#         return self.__blance
    
# s1=bank("ali",20000)
# s1.deposit(10000)
# s1.withdraw(100)
# print(s1.get_blance())

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  

#     @property
#     def password(self):
#         return self.__password

#     @password.setter
#     def password(self, new_pass):
#         if len(new_pass) >= 6:
#             self.__password = new_pass
#             print("Password updated successfully!")
#         else:
#             print("Password must be at least 6 characters long.")

# s1=User("ali","sar123")
# print(s1.password)
# s1.password="234fggg"
# print(s1.password)



        









        





    