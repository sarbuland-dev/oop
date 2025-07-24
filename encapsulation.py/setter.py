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
    def set_bank_blance(self,new_blance):
        if 0<=new_blance<=5000:
            self.__bank_blance=new_blance
        else:
            print("invalid entry")
    
s1=Bank("ali",12342334,2000)
print(s1.get_bank_blance())
s1.set_bank_blance(3000)
# print(s1.get_bank_blance())
# s1.set_bank_blance(6000)
# print(s1.get_bank_blance())