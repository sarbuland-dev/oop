class Bank:
    @staticmethod
    def __init__(self,ower,bank_account,bank_blance):
        self.ower=ower
        self.bank_account=bank_account
        self.bank_blance=bank_blance
    def details(self):
        print("ower",self.ower)
        print("bank_account",self.bank_account)
        print("bank_blance",self.bank_blance)

Bank.details("ali",12352342,7000)

    