class Solution(object):
    def bitwiseComplement(self, n):
        binary=bin(n)[2:]
        res=""
        for ch in binary:
            if(ch=='0'):
                res+='1'
            else:
                res+='0'
        return int(res,2)