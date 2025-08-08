class Solution(object):
    def isPalindrome(self, x):
        if (str(x))==(str(x)[::-1]):
         print("its a palindrome")
        else:
            print("not")

s=Solution()
print(s.isPalindrome(-121))

# method to reverse number without using methods 

class solution:
    def show(self,num):
        number_str=str(num)
        reverse_str=""
        for i in range(len(number_str)-1,-1,-1):
            reverse_str+=number_str[i]
        return reverse_str

s=solution()
print(s.show(12345))


class solution:
    def show(self,chr):
        lock=[]
        for ch in chr:
          if ch in "([{":
            lock.append(ch)
          else:
            if ch==")"and lock[-1]!="(":
                return False
            elif ch=="]"and lock[-1]!="[":
                return False
            elif ch=="}"and lock[-1]!="{":
                return False
            lock.pop()
        return not lock
        
s=solution()
print(s.show("()"))

