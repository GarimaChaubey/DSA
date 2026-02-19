class Solution(object):
    def countBinarySubstrings(self, s):
        result=0
        curr=1
        prev=0

        for i in range(1, len(s)):
            if(s[i]==s[i-1]):
                curr+=1
            else:
                result+=min(curr,prev)
                prev=curr
                curr=1
            
        return result+min(curr,prev)