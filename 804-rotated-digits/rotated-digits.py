class Solution:
    def rotatedDigits(self, n):
        
        valid = {0,1,2,5,6,8,9}
        change = {2,5,6,9}
        
        def is_good(num):
            has_change = False
            
            while num > 0:
                d = num % 10
                
                if d not in valid:
                    return False
                
                if d in change:
                    has_change = True
                
                num //= 10
            
            return has_change
        
        count = 0
        
        for i in range(1, n+1):
            if is_good(i):
                count += 1
        
        return count