        class car:
        def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        def full_name(self):
        return(f"{self.brand} {self.model}")   

        my_car=car("range rover","rx13")
        print(my_car.brand)
        print(my_car.model)

        my_new_car=car("tesla","nelon")
        print(my_new_car.brand)
        print(my_new_car.model)

        class Student:
        def __init__(self,name,age,rollnumber):
        self.name=name
        self.age=age
        self.rollnumber=rollnumber
        def show_data(self):
        print("Name: ",self.name)
        print("age:",self.age)
        print("rollnumber:  ",self.rollnumber)

        s1=Student("ali",21,12345)
        s2=Student("ahmad: ",23,123321)
        print("name: " , s1.name,"age:",  s1.age,"rollnumber",  s1.rollnumber)
        print("_______________________________")
        print("name: " , s2.name,"age:",  s2.age,"rollnumber",  s2.rollnumber)

        class Bank:
        def __init__(self,ower,bank_account,bank_blance):
        self.ower=ower
        self.bank_account=bank_account
        self.bank_blance=bank_blance
        def details(self):
        print("ower",self.ower)
        print("bank_account",self.bank_account)
        print("bank_blance",self.bank_blance)

        s1=Bank("ali",1235634556776,2000)
        # print("Name; ",s1.ower,"acount: ",s1.bank_account,"blance",s1.bank_blance)
        s1.details()