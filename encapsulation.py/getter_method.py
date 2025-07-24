class Bank:
    def __init__(self,ower,bank_account,bank_blance):
        self.ower=ower
        self.bank_account=bank_account
        self.__bank_blance=bank_blance
    def details(self):
        print("ower",self.ower)
        print("bank_account",self.bank_account)
        print("bank_blance",self.__bank_blance)
    def get_bank_blance(self):
        return self.__bank_blance
    
    
s1=Bank("ali",12342334,2000)
print(s1.get_bank_blance())

