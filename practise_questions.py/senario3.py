# class add:
#     def __init__(self,a,b,c=0):
#         return a+b+c
    
# x=add()
# print(x.__init__(23,34,5))

class Calculator:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c


obj = Calculator()

# 2 numbers
print("Sum of 2 numbers:", obj.add(5, 10))        # Output: 15

# 3 numbers
print("Sum of 3 numbers:", obj.add(5, 10, 15))     # Output: 30
