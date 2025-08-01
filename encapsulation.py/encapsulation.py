class Bank:
    def __init__(self,ower,bank_account,bank_blance):
        self.ower=ower
        self.bank_account=bank_account
        self.__bank_blance=bank_blance
    def details(self):
        print("ower",self.ower)
        print("bank_account",self.bank_account)
        print("bank_blance",self.__bank_blance)
        
# ya second class inheritance ko show karti ha
class Subbank(Bank):                                        
    def __init__(self,ower,bank_account,bank_blance,location):
        super().__init__(ower,bank_account,bank_blance)
        self.location=location
    def show_more(self):
        # self.details()              if parent ko nichy lana ho tu
        print("location",self.location)
    
        

s1=Subbank("ali",1235634556776,2000,"talwandi")
# print("Name; ",s1.ower,"acount: ",s1.bank_account,"blance",s1.bank_blance)
s1.show_more()
s1.details()
# s1.__bank_blance     ager asy likhy gy tu error ay ga ku ky hum ny bank blance ko encapsuled kar diya ha