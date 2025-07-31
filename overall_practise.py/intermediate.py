class student:
    def __init__(self,name):
        self.name=name
        self.course=[]
    def apply_course(self):
        print("1: math")
        print("2: physics")
        print("3: urdu")
        print("4: chemistry")
        print("5: english")
        choice=input("enter your enrollment subjects  ")
        choice_map={
            "1":"math",
            "2":"physics",
            "3":"urdu",
            "4":"chemistry",
            "5":"english"}
        choice_list=choice.split(",")
        for chr in choice_list:
            course=choice_map.get(chr.strip())
            if course:
                self.course.append(course)
            else:
                print("invlid")
        print(f"{self.name} applied in\n {",".join(self.course)}")
        
        
        
        

s1=student("ali")
s1.apply_course()
