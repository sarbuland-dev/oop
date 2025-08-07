# class Solution:
#     def twoSum(self, nums, target,):
#         for i in range(len(nums)):
#             for j in (i+1,len(nums)):
#                 if i+j==target:
#                     return([i,j])

# x=Solution()
# x.twoSum([45,2,89,4,5,6,72,3,4],8)

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # Example usage
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

# class Solution(object):
#     def isValid(self, s):
#         if "()":
#          return True
#         elif "[]":
#          return True
#         elif "{}":
#          return True
#         elif "()[]{}":
#          return True
#         else:
#             return False
        
# s=Solution()
# print(s.isValid("(]"))

        
        
class Solution:
    def decimal(self,number):
        int_part=[]
        desimal_part=[]
        decimal_number=number/10
        
        str_decimal_number=str(decimal_number)
        if "."in str_decimal_number:
         decimal_value=str_decimal_number.split(".")[1]
         desimal_part.append(decimal_value)
         int_part.append(int(decimal_number))
         return decimal_value,int(decimal_number)
        
        print( desimal_part()*int_part())
   
    
        
s=Solution()
print(s.decimal(23456))


x=[2345]
# number=[]
# for i in range(len(x)):
#     for j in (i+1,len(x)):
#         if i<j:
#          number.append(x[i],x[j])
#         else:
#            break

         
        
        