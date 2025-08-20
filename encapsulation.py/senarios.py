class Bankaccount:
    def __init__(self,account_number):
        self.account=account_number
        self.__balance=0
        
        
    def show(self):
        return f"your account number is {self.account} and your account balance is {self.__balance}"
    def depost(self):
        amount=float(input("enter your amount "))
        self.__balance+=amount
        
        return self.__balance
    def withdraw(self):
        amount=float(input("enter your amount "))
        if amount<=self.__balance:
            self.__balance-=amount
            
            return self.__balance
    def get_balance(self):
        return self.__balance
    def set_balance(self):
        amount=float(input("enter your amount "))
        new_amount=amount
        if new_amount>=0:
             self.__balance =new_amount
             return self.__balance
s1=Bankaccount(12345)
print(s1.depost())
print(s1.withdraw())
print(s1.get_balance())
print(s1.set_balance())
            
            
class Cart:
    def __init__(self):
        self.__itmes=[]
    def add(self):
        product=input("enter your product name ")
        self.__itmes.append(product)
        return f" your {product} add and list of product are {self.__itmes}"
    def remove(self):
        x=input("enter your product name ")
        self.__itmes.remove(x)
        return f"{self.__itmes}"
    def get_itmes(self):
        return self.__itmes
    
s1=Cart()
print(s1.add())
print(s1.remove())
print(s1.get_itmes())
             
        