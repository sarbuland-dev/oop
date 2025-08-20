class Account:
    def __init__(self,account_number,balance):
        self.number=account_number
        self.balance=balance
    def show(self):
        return {"account number":self.number,"balance":self.balance}
        
    
class SavingAccount(Account):
    def __init__(self,account_number,balance,text_rate,withdraw_limit):
        super().__init__(account_number,balance,)
        self.text=text_rate
        self.limit=withdraw_limit
    def show(self):
        base_show=super().show()
        base_show.update({"text":self.text,"withdraw":self.limit})
        return base_show

class PremiumSavingsAccount(SavingAccount):
    def __init__(self,text_rate,withdraw_limit,offers):
        super().__init__(text_rate,withdraw_limit)
        self.offer=offers
        
s1=SavingAccount(12345,3000,30,10000)
print(s1.show())

        