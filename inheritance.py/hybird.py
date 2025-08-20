class Device:
    def __init__(self,id,stauts):
        self.id=id
        self.st=stauts
    def device_show(self):
        return {"id":self.id,"stauts":self.st}
    
class Smartlight(Device):
    def __init__(self, id, stauts,brigtness,colour):
        super().__init__(id, stauts)
        self.brigtness=brigtness
        self.colour=colour
    def smart_show(self):
        base=super().device_show()
        base.update({"brigtness":self.brigtness,"colour":self.colour})
        return base
        
class Thermlight(Device):
    def __init__(self, id, stauts,temperature):
        super().__init__(id, stauts)
        self.tem=temperature
        
    def therm_show(self):
        base=super().device_show()
        base.update({"temperature":self.tem})
        return base

class Effictive:
    def __init__(self, saving):

        self.saving=saving
    def effictive_show(self):
        return {"effictiveness":self.saving}
    
class Eco(Smartlight,Effictive):
    def __init__(self, id, stauts,brigtness,colour,saving):
        Smartlight.__init__(self,id, stauts,brigtness,colour)
        Effictive.__init__(self,saving)
        
    def eco_show(self):
        base1=Smartlight.smart_show(self)
        base=Effictive.effictive_show(self)
        return base1,base
    
    
s1=Eco(1234,"active","high","blue",200)
print(s1.eco_show())
        
    


        