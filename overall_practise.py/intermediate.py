# class student:
#     def __init__(self,name):
#         self.name=name
#         self.course=[]
#     def apply_course(self):
#         print("1: math")
#         print("2: physics")
#         print("3: urdu")
#         print("4: chemistry")
#         print("5: english")
#         choice=input("enter your enrollment subjects  ")
#         choice_map={
#             "1":"math",
#             "2":"physics",
#             "3":"urdu",
#             "4":"chemistry",
#             "5":"english"}
#         choice_list=choice.split(",")
#         for chr in choice_list:
#             course=choice_map.get(chr.strip())
#             if course:
#                 self.course.append(course)
#             else:
#                 print("invlid")
#         print(f"{self.name} applied in\n {",".join(self.course)}")
        
        
        
        

# s1=student("ali")
# s1.apply_course()


# Scenario 1: Employee Management System
# Problem:
# You are designing an employee management system for a company. Each Employee has a name, ID, and salary. There are different types of employees: Manager, Developer, and Intern.

# Task:

# Design a class structure using inheritance.

# Each subclass should have a method calculate_bonus() that returns a different percentage of the salary.

# Bonus: Use a class method to keep track of the number of employees created

# class emploee:
#     emploee_count=0
#     def __init__(self,name,id,salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
#         emploee.emploee_count+=1
#     def details(self):
#         print("Name",self.name)
#         print("id ",self.id)
#         print("salary ",self.salary)

# class Manager(emploee):
#     def __init__(self,name,id,salary,percentage):
#         super().__init__(name,id,salary)
        
#         self.percentage=percentage
#     def details(self):
#          super().details()
#          print("percentage",self.percentage)
#          month_bounse=(self.salary*self.percentage)/100
#          anual_bounse=month_bounse*12
#          print(f"you have salary {self.salary} and bouns {anual_bounse}")

# class develper(emploee):
#     def __init__(self,name,id,salary,percentage):
#         super().__init__(name,id,salary)
        
#         self.percentage=percentage
#     def details(self):
#          super().details()
#          print("percentage",self.percentage)
#          month_bounse=(self.salary*self.percentage)/100
#          anual_bounse=month_bounse*12
#          print(f"you have salary {self.salary} and bouns {anual_bounse}")

# class intern(emploee):
#     def __init__(self,name,id,salary,percentage):
#         super().__init__(name,id,salary)
        
#         self.percentage=percentage
#     def details(self):
#          super().details()
#          print("percentage",self.percentage)
#          month_bounse=(self.salary*self.percentage)/100
#          anual_bounse=month_bounse*12
#          print(f"you have salary {self.salary} and bouns {anual_bounse}")
         
# s1=Manager("ali",12789,12000,20)
# s1.details()
# print("______________________________________")
# s2=develper("Ahmad ",12789,10000,20)
# s2.details()
# print("______________________________________")
# s2=intern("hamaz ",12789,7000,10)
# s2.details()
# print(f"total emploee created {emploee.emploee_count}")

#  Scenario 2: Inventory System for an Online Store
# Problem:
# You’re building an inventory system where each Product has a name, price, and quantity. The store sells Books and Electronics.

# Task:

# Implement a base class Product and subclasses for Book and Electronic.

# Use properties to ensure price and quantity can’t be negative.

# Add a method apply_discount() in the base class and override it in Book (books get extra 10% off).

# Bonus: Implement __str__ and __repr__ methods for debugging and display

# class product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def details(self):
#         print("Name:",self.name)
#         print("price",self.price)
#         print("quantity",self.quantity)

# class book(product):
#     def __init__(self,name,price,quantity,discount_percent):
#         super().__init__(name,price,quantity)
#         self.discount_percent=discount_percent
#     def details(self):
#          super().details()
#          print("discount",self.discount_percent)
#          quantity_price=self.price*self.quantity
#          print(f"your {self.quantity} books price is {quantity_price} ")
#          discount=(quantity_price*self.discount_percent)/100
#          final_price=quantity_price-discount
#          print(f"your total price is {final_price}")

# s1=book("the hate",1200,5,10)
# s1.details()

#  Scenario 3: Bank System with Transaction Logging
# Problem:
# You are creating a simple banking system with a BankAccount class. Users should be able to deposit, withdraw, and check balance. Every transaction should be logged.

# Task:

# Keep a private balance attribute.

# Log all transactions (e.g., deposit, withdraw) using a list.

# Add a method show_history() to print transaction logs.

# Bonus: Use a mixin class for logging to allow reusability
              
# class bankAccount:

    
#     def __init__(self,name,account_number,balance):
#         self.name=name
#         self.account_number=account_number
#         self.__balance=balance
#         self.__new_balance=0
#         self.log=[]
#     def details(self):
#         print("Name",self.name)
#         print("Account number",self.account_number)
#         print("balance",self.__balance)
#     def deposit(self,amount):
#         if 0<=amount<=20000:
#             deposit=self.__balance+amount
#             self.__new_balance=deposit
#             self.log.append(f"deposit amont is {deposit} and new balance is {self.__new_balance}")
            
#             print("your deposit valu is ",amount)
#             print(f"you {amount} is added and your total amont is {deposit}")
#     def withdraw(self,amount):
#         if 0<=amount<=20000:
#             withdraw=self.__new_balance-amount
#             self.log.append(f"withdraw amont is {amount} and balance remain {withdraw}")
#             print("your withdraw  amount is ",amount)
#             print(f"you {amount} is withdraw and your total amont is {withdraw}")
#     def get_balance(self):
#         print(self.__balance)
#     def get_new_balance(self):
#         print(self.__new_balance)
#     def set_balance(self,amount):
        
#         self.__balance=amount
#         print(amount)
#     def show_histry(self):
#         if not self.log:
#             print("not any transaction histry")
#         else:
#             print(self.log)
        
# s1=bankAccount("ali",123456,1000)
# s1.details()
# s1.deposit(2000)
# s1.withdraw(2000)
# s1.get_balance()
# s1.set_balance(5000)
# s1.deposit(5000)
# s1.show_histry()
# print("_______________________________-")
# s2=bankAccount("ahmad",34567,4000)
# s2.details()
# s2.deposit(4000)
# s2.withdraw(1000)
# print("________________________________")
# s2.show_histry()


class vehical:
    
    def __init__(self):
        print("Welcom to our services!")
        self.car_bill=[]
        self.Turck_bill=[]
        self.bike_bill=[]
        self.car_balance=0
        self.truck_balance=0
        self.bike_balance=0

    def details(self):
        
        print("choice your vehical type ")
        print("1: car ")
        print("2: truck")
        print("3: bike ")
        print("0: Exit  ")
        vehical_type=int(input("enter your vehical type  "))
        if 1<=vehical_type<=3:
         while True:
            if vehical_type==1:
                print(" your car menu ")
                print("1: oil change___230Rs/-")
                print("2: car wash___200Rs/-")
                print("3: headlight repairing__2000Rs/-")
                print("4: internal repairing___1500Rs/-")
                print("5: back to vechical menu! ")
                choices=(input("Enter your choice (1,2,3,4,5)  ")).split(",")
                for choice in choices:
                 choice=choice.strip() 
                 if choice=="1":
                    self.car_balance+=230
                    self.car_bill.append(("oil change", 230))
                 elif choice=="2":
                    self.car_balance+=200
                    self.car_bill.append(("car wash", 200))
                 elif choice=="3":
                    self.car_balance+=2000
                    self.car_bill.append(("headlight repairing", 2000))
                 elif choice=="4":
                    self.car_balance+=1500
                    self.car_bill.append(("internal repairing", 1500))
                 elif choice=="5":
                    print(self.details())
                    break
                 else:
                    print("invalid option ")
                print(f"Your total bill of car service  {self.car_balance}/-")
            elif vehical_type==2:
               while True:
                  print("your Truck menu is: ")
                  print("1: oil change___400Rs/-")
                  print("2: truck wash___1000Rs/-")
                  print("3: headlight repairing__3000Rs/-")
                  print("4: internal repairing___2000Rs/-")
                  print("5: back to vechical menu! ")
                  choices=input("Enter your choice (1,2,3,4,5)  ").split(",")
                  for choice in choices:
                     choice=choice.strip()
                     if choice=="1":
                        self.truck_balance+=400
                        self.Turck_bill.append(("oil change", 400))
                     elif choice=="2":
                        self.truck_balance+=1000
                        self.Turck_bill.append(("truck wash", 1000))
                     elif choice=="3":
                        self.truck_balance+=3000
                        self.Turck_bill.append(("headlight repairing", 3000))
                     elif choice=="4":
                        self.truck_balance+=2000
                        self.Turck_bill.append((" internal repairing", 2000))
                     elif choice=="5":
                        print(self.details())
                        break
                     else:
                        print("invalid option ")
                  print(f"Your total bill of truck service  {self.truck_balance}/-")
            elif vehical_type==3:
                     while True:
                      print("your bike menu is: ")
                      print("1: oil change___100Rs/-")
                      print("2: bike wash___150Rs/-")
                      print("3: headlight repairing__2000Rs/-")
                      print("4: internal repairing___1500Rs/-")
                      print("5: back to vechical menu! ")
                      choices=input("Enter your choice (1,2,3,4,5)  ").split(",")
                      for choice in choices:
                          choice=choice.strip()
                          if choice=="1":
                           self.bike_balance+=100
                           self.bike_bill.append(("oil change", 100))
                          elif choice=="2":
                           self.bike_balance+=150
                           self.bike_bill.append(("bike wash" ,150))
                          elif choice=="3":
                           self.bike_balance+=2000
                           self.bike_bill.append(("headlight repairing" ,2000))
                          elif choice=="4":
                           self.bike_balance+=1500
                           self.bike_bill.append(("internal repairing" , 1500))
                          elif choice=="5":
                           print(self.details())
                           break
                          else:
                           print("invalid option ")
                     
                      print(f"Your total bill of bike service  {self.bike_balance}/-")
               
                    

                     

                  
                      
                    

                   
        elif vehical_type==0:
           print(f"Your car bill of  service  {self.car_bill}/-")
           print(f"Your truck bill of  service  {self.Turck_bill}/-")
           print(f"Your bike bill of  service  {self.bike_bill}/-")
           total=self.car_balance+self.truck_balance+self.bike_balance
           print(f"your total bill is {total} ")
           print("Takecare! goodbye ")
           exit()
                


s1=vehical()
s1.details()
