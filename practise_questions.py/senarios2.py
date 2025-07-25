class Bankaccount:
    def __init__(self,name,blance):
        self.name=name
        self.__blance=blance
    def deposit(self,amount):
        print("name",self.name)
        if amount>=0:
            self.__blance+=amount
            print(f"{amount}has been deposit successfully!!")
        else:
            print("invalid transaction")
    def get_blance(self):
        return self.__blance
    
x=Bankaccount("sarbuland",120)
x.deposit(10000)
print(x.get_blance())
            
        
        