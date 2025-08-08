class cart:
    def __init__(self):
        print("_"*40)
        print("welcome to SB shooping mall")
        print("_"*40)
        self.men_bill=[]
        self.women_bill=[]
        self.men_balance=0
        self.women_balance=0
        login=[]
    def details(self):
        
        print("_"*40)
        self.name=(input("Enter your name  ")).capitalize()
        print("_"*40)
        print(f" Hello! Mr{self.name}")
        print("_"*40)
        print("your shopping cart menu is here!!! ")
        while True:
         print("Enter your gender  ")
         print("1: Men")
         print("2: Women ")
         print("3: discount upto 20% ")
         print("4: Exit")
         print("-"*40)
         choice=int(input("Enter your choice  "))
         print("-"*40)
         if choice==1:
            print("Men menu is here!!")
            print("1: pent shirt  2000/-")
            print("2: polo shirt  1000/-")
            print("3: sahlwar kamiz  4000/-")
            print("4: kurta  1500/-")
            print("5: back to menu ")
            print("_"*40)

            choice=input("Enter your shopping identites ")
            print("_"*40)
            for i in choice:
               i=i.strip()
               if i=="1":
                  self.men_balance+=2000
                  self.men_bill.append(("pent shirt",2000))
               elif i=="2":
                  self.men_balance+=1000
                  self.men_bill.append(("polo shirt",1000))
               elif i=="3":
                  self.men_balance+=4000
                  self.men_bill.append(("sahlwar kamiz",4000))
               elif i=="4":
                  self.men_balance+=1500
                  self.men_bill.append(("kurta",1500))
               elif i==5:
                  self.details()
                  break
            print(">"*40)   
            print(f"your total bill is {self.men_balance}PKR  and details are {self.men_bill} ")
            print("now if you want discount check now!!!")
            print(">"*40)
         elif choice==2:
            print("1: dressing ")
            print("2: makeup ")
            print("3: Exit")
            print("_"*40)
            choice=int(input("enter your choice "))
            print("_"*40)
            if choice==1:
             print("your women shopping menu is here")
             print("1: women pent shirt  4000/-")
             print("2: women polo shirt  5000/-")
             print("3: women sahlwar kamiz  1000/-")
             print("4: women kurta  2300/-")
             print("5: back to menu ")
             print("_"*40)
             choice=input("Enter your shopping identites ")
             print("_"*40)
             for i in choice:
               i=i.strip()
               if i=="1":
                  self.women_balance+=4000
                  self.women_bill.append((" women pent shirt",4000))
               elif i=="2":
                  self.women_balance+=5000
                  self.women_bill.append(("women polo shirt",5000))
               elif i=="3":
                  self.women_balance+=1000
                  self.women_bill.append(("women sahlwar kamiz",1000))
               elif i=="4":
                  self.women_balance+=2300
                  self.women_bill.append(("women kurta",2300))
               elif i==5:
                  self.details()
                  break
            elif choice==2:
               print("your makeup menu is here!!")
               print("1: Foundation  2000")
               print("2: Concealer  3000")
               print("3: Mascara  2500")
               print("4: Lipstick  1000")
               print("5: back to main menu ")
               print("_"*40)
               choice=input("Enter your choice ")
               print("_"*40)
               for i in choice:
                  i=i.strip()
                  if i=="1":
                     self.women_balance+=2000
                     self.women_bill.append(("Foundation",2000))
                  elif i=="2":
                     self.women_balance+=3000
                     self.women_bill.append(("Concealer ",3000))
                  elif i=="3":
                     self.women_balance+=2500
                     self.women_bill.append(("Mascara ",2500))
                  elif i=="4":
                     self.women_balance+=1000
                     self.women_bill.append(("Lipstick ",1000))
                  
                  elif i=="5":
                     self.details()
            
            elif choice==3:
             exit()
            print(">"*40)
            print(f"your total bill is {self.women_balance}PKR  and details are {self.women_bill} ")
            print("now if you want discount check now!!!")
            print(">"*40)
         elif choice==3:
            print("welcom to discount section ")
            print("1: Men discount section")
            print("2: women discount section ")
            print("3: both discount section")
            print("_"*40)
            choice=int(input("Enter your choice "))
            print("_"*40)
            if choice==1:
              cal= (self.men_balance*20)/100
              discount=self.men_balance-cal
              print("_"*40)
              print(f"congratulations!! now your total bill now {discount}")
              print("_"*40)
            elif choice==2:
                cal= (self.women_balance*20)/100
                discount_women=self.women_balance-cal
                print("_"*40)
                print(f"congratulations!! now your total bill now {discount_women}")
                print("_"*40)
            elif choice==3:
               total=self.men_balance+self.women_balance
               cal=(total*20)/100
               discount= total-cal
               print("_"*40)
               print(f"congratulations!! now your total bill now {discount}")
               print("_"*40)
               
               

         elif choice==4:
            
            print("<"*40)
            print(f"your total bill {self.men_balance} and details {self.men_bill}")
            print(f"your total bill {self.women_balance} and details {self.women_bill}")
            print("<"*40)
            exit()

    
        
s1=cart()
print(s1.details())