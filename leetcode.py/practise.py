
# twosum

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# x = Solution()
# print(x.twoSum([22, 2, 7, 5, 67, 4], 9))



# class Solution(object):
#     def isPalindrome(self, x):
#         if (str(x))==(str(x)[::-1]):
#          print("its a palindrome")
#         else:
#             print("not")

# s=Solution()
# print(s.isPalindrome(-121))



        
        
# class Solution:
#     def decimal(self,number):
#         int_part=[]
#         desimal_part=[]
#         decimal_number=number/10
        
#         str_decimal_number=str(decimal_number)
#         if "."in str_decimal_number:
#          decimal_value=str_decimal_number.split(".")[1]
#          desimal_part.append(decimal_value)
#          int_part.append(int(decimal_number))
#          return decimal_value,int(decimal_number)
        
#         print( desimal_part()*int_part())
   
    
        
# s=Solution()
# print(s.decimal(23456))



# method to reverse number without using methods 

# class solution:
#     def show(self,num):
#         number_str=str(num)
#         reverse_str=""
#         for i in range(len(number_str)-1,-1,-1):
#             reverse_str+=number_str[i]
#         return reverse_str

# s=solution()
# print(s.show(12345))





# class solution:
#     def show(self,chr):
#         lock=[]
#         for ch in chr:
#           if ch in "([{":
#             lock.append(ch)
#           else:
#             if ch==")"and lock[-1]!="(":
#                 return False
#             elif ch=="]"and lock[-1]!="[":
#                 return False
#             elif ch=="}"and lock[-1]!="{":
#                 return False
#             lock.pop()
#         return not lock
        
# s=solution()
# print(s.show("()"))

class Solution:
      
   def isValid(self,num):
      
      i=0
      for j in range(1,len(num)):
        if num[i]!=num[j]:
           i+=1
           num[i]=num[j]
      return i+1

            
      
   
s=Solution()
print(s.isValid([1,1,2,1,2]))
      
         
        
        
         
                


        
        
         
         
        
        