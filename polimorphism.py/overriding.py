class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):  # Overriding
        print("This is child class")

c = Child()
c.show()
c = Parent()
c.show()
