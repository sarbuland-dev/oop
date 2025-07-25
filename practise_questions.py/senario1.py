class person:
    def __init__(self,name):
        self.name=name
    def details(self,):
            print("Name",self.name)
                  

class emploee(person):
    def __init__(self,name,work):
        super().__init__(name)
        self.work=work
    def details(self):
         super().details()
         print("work",self.work)

x=person("ahmad")
x.details()
x=emploee("ahmad","software")
x.details()
