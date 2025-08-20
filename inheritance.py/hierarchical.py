class Person:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def person_show(self):
        return {"name":self.name,"age":self.age,"id":self.id}
    
class Student(Person):
    def __init__(self,name,age,id,courses,GPA):
        super().__init__(name,age,id)
        self.course=courses
        self.gpa=GPA
    def student_show(self):
        base_show=super().person_show()
        base_show.update({"course":self.course,"GPA":self.gpa})
        return base_show

class Professor(Person):
    def __init__(self,name,age,id,dep,salary):
        super().__init__(name,age,id)
        self.dep=dep
        self.salary=salary
    def dep_show(self):
        base_show=super().person_show()
        base_show.update({"department":self.dep,"salary":self.salary})
        return base_show
        
s1=Professor("ali",23,2345,"BSSE",23000)
print(s1.dep_show())  
        