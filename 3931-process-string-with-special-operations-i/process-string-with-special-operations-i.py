class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = []
        
        for ch in s:
            
            if 'a' <= ch <= 'z':
                res.append(ch)
            
            elif ch == '*':
                if res:
                    res.pop()
            
            elif ch == '#':
                res.extend(res)
            
            else:  
                res.reverse()
        
        return "".join(res)