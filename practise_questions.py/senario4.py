class counter:
    def show(self,data):
        if isinstance(data,str):
            print("str dected")
            print(len(data))
        elif isinstance(data,list):
            print(len(data))
        else:
            print("invail")

x=counter()
x.show("sasasasadsfsfsgsgghh")
x.show([1,2,3,4,5,6,7,78,9])
