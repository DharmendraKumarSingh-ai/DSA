class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x<0 else 1
        x = abs(x)

        rev = 0 

        while x != 0:
            
            num = x%10
            rev = rev * 10+ num
            x = x//10
        rev = rev*sign

        if rev in range(-2**31,(2**31)-1):
            return rev
        else:
            return 0

        
        
    