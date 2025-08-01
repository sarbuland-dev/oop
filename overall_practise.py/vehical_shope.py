class vehical:
    
    def __init__(self):
        print("="*20)
        print("Welcom to our services!")
        print("="*20)
        self.car_bill=[]
        self.Turck_bill=[]
        self.bike_bill=[]
        self.car_balance=0
        self.truck_balance=0
        self.bike_balance=0

    def details(self):
        print("="*20)
        print("choice your vehicle type ")
        print("="*20)
        print("1: car ")
        print("2: truck")
        print("3: bike ")
        print("0: Exit  ")
        print("="*20)
        vehical_type=int(input("enter your vehicle type  "))
        print("="*20)
        if 1<=vehical_type<=3:
         while True:
            if vehical_type==1:
                print("="*20)
                print(" your car menu ")
                print("="*20)
                print("1: oil change___230Rs/-")
                print("2: car wash___200Rs/-")
                print("3: headlight repairing__2000Rs/-")
                print("4: internal repairing___1500Rs/-")
                print("5: back to vechicle menu! ")
                print("="*20)
                choices=(input("Enter your choice (1,2,3,4,5)  ")).split(",")
                print("="*20)
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
                print("-"*10)    
                print(f"Your total bill of car service  {self.car_balance}/-")
                print("-"*10)  
            elif vehical_type==2:
               while True:
                  print("="*20)
                  print("your Truck menu is: ")
                  print("="*20)
                  print("1: oil change___400Rs/-")
                  print("2: truck wash___1000Rs/-")
                  print("3: headlight repairing__3000Rs/-")
                  print("4: internal repairing___2000Rs/-")
                  print("5: back to vechicle menu! ")
                  print("="*20)
                  choices=input("Enter your choice (1,2,3,4,5)  ").split(",")
                  print("="*20)
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
                  print("-"*10)      
                  print(f"Your total bill of truck service  {self.truck_balance}/-")
                  print("-"*10)  
            elif vehical_type==3:
                     while True:
                      print("="*20)
                      print("your bike menu is: ")
                      print("="*20)
                      print("1: oil change___100Rs/-")
                      print("2: bike wash___150Rs/-")
                      print("3: headlight repairing__2000Rs/-")
                      print("4: internal repairing___1500Rs/-")
                      print("5: back to vechicle menu! ")
                      print("="*20)
                      choices=input("Enter your choice (1,2,3,4,5)  ").split(",")
                      print("="*20)
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
                      print("-"*10)  
                      print(f"Your total bill of bike service  {self.bike_balance}/-")
                      print("-"*10)  
               
                    

                     

                  
                      
                    

                   
        elif vehical_type==0:
           print("_"*30)
           print(f"Your car bill of  service  {self.car_bill}/-")
           print("_"*30)
           print(f"Your truck bill of  service  {self.Turck_bill}/-")
           print("_"*30)
           print(f"Your bike bill of  service  {self.bike_bill}/-")
           print("_"*30)
           total=self.car_balance+self.truck_balance+self.bike_balance
           print(":"*40)
           print(f"your total bill is {total} ")
           print(":"*40)
           print("Takecare! goodbye ")
           exit()
                


s1=vehical()
s1.details()