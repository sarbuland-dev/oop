class Transport_ticket:
    def __init__(self,name,person_id):
     self.name=name
     self.person_id=person_id
    def detail(self):
        print(f"{self.name},{self.person_id}")
        
class bus(Transport_ticket):
    def __init__(self,name,person_id,bus_site):
        super().__init__(name,person_id)
        self.bus_site=bus_site
    def show(self):
        print(f"{self.name},{self.person_id},{self.bus_site}")
        
s1=bus("ahmad",18923,12)
s1.show()

class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def account_type(self):
        return "General Account"

class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"

class CheckingAccount(BankAccount):
    def account_type(self):
        return "Checking Account"

class LoanAccount(BankAccount):
    def account_type(self):
        return "Loan Account"

# Example
accounts = [SavingsAccount(101, 5000), CheckingAccount(102, 2000), LoanAccount(103, -10000)]
for acc in accounts:
    print(f"Acc #{acc.acc_no}: {acc.account_type()}")

     
        