class Solution(object):
    def minOperations(self, s):
        n=len(s)

        start_with_0=0
        start_with_1=0
        
        for i in range(n):
            if(i%2==0):
                if(s[i]=='0'):
                    start_with_1+=1
                else:
                    start_with_0+=1
            else:
                if (s[i]=='1'):
                    start_with_1+=1
                else:
                    start_with_0+=1

        return min(start_with_0, start_with_1)
        