
import random
class bank_menu:
    def __init__(self):
        print("welcome to SB bank \n Har faard ka bharosa!")
        self.check_account=[]
        self.password=[]
        self.balance={}
    def menu(self):
        print("Select your option below")
        print("1: Open new account ")
        print("2: Balance Inquary ")
        print("3: Transactions ")
        choice=int(input("enter your option "))
        print("Your option is ",choice)
        if choice==1:
            print("You choose \open new account")
            FirstName=input("Enter your First Name\n")
            FirstName.capitalize()
            Firstindex=FirstName[0].upper()
            
            LastName=input("Enter your Last Name\n")
            LastName.capitalize()
            Lastindex=LastName[0].upper()
            fullname=f"{FirstName.capitalize()} {LastName.capitalize()}"
            print(f"A o A! {fullname} ")
            while True:
             account=random.randint(1000,5555)
             account=f"{Firstindex}{Lastindex}{account}"
             if account not in self.check_account:
                 self.check_account.append(account)
                 print(f"Mr.{fullname} ! your accound number is  {account} ")
                 break
             else:
         
                 print(" this account is already created! plz wait new account is generating ")
            while True:
             account_input=(input("enter your accout number which is created by SB bank authority     "))
             if account_input==account:
                password_input=int(input("enter your password(1-4) digits  "))
                if 1000<=password_input<=9999:
                    if password_input not in self.password:
                        self.password.append(password_input)
                        self.balance[account]=0
                        print("password save successfully!")
                        break
                    else:
                        print("password already exist try new one! ")
                    
            print(f" your account details are \n Name: {fullname}\n Account number: {account}\n password: {password_input}")  
        else:
           print("creat account first !!")
           exit()
        
        print("If you created account successfully!  select the option below ")
        print("1: Balance Inquary ")
        print("2: Transactions")
        choice=int(input("Enter your choice "))
        if choice==1:
           print("you choice Balance Inquary ")
           account_check=(input("enter your SB account  "))
           if account_check in self.check_account:
              
              password_check=int(input("Enter your password "))
              if password_check in self.password:
                 balance=self.balance
                 print(f"your balance is {balance}")
              else:
                 print("wrong password!!")
           else:
              print("Account not found!!")
        elif choice==2:
           while True:
            print ("you choice transaction ")
            trans_check=(input("Enter your account number  "))
            if trans_check in self.check_account:
               trans_pass=int(input(("Plz enter your password  ")))
               if trans_pass in self.password:

               
                 print("Select option below ")
                 print("1: Deposit money ")
                 print("2: withdraw money ")
                 print("3: Exit")
                 choice=int(input("enter your choice  "))
                 if choice==1:
                     print("you choose to deposit ")
                     amount=int(input("enter your amount to deposit  "))
                     self.balance[account]+=amount
            
                     print(f"your deposit amount {amount} added to your bank balance successfully!!")
                 elif choice==2:
                   print("you selected withdraw money ")
                   amount=int(input("enter your amount "))
                   if 0<amount<=self.balance[account]:
                      self.balance[account]-=amount
               
                      print(f"you withdraw {amount}  and current balance is",self.balance)
                   else:
                     print("insufficient balance !!!")
                 
                 elif choice==3:
                    exit()
                  
               else:
                  print("wrong password!!")    
           
           else:
              print("accound not found")

                 
              
             
         
              

         



        






s1=bank_menu()
s1.menu()
