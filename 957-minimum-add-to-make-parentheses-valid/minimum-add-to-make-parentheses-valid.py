class Solution(object):
    def minAddToMakeValid(self, s):
        b = 0
        ans = 0

        for ch in s:

            if ch == '(':
                b += 1

            else:
                if b > 0:
                    b-= 1
                else:
                    
                    ans += 1

        ans += b

        return ans
        