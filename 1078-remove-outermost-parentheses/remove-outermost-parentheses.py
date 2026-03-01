class Solution(object):
    def removeOuterParentheses(self, s):
        ans=[]
        cnt=0
        for ch in s:
            if ch == '(':
                if cnt > 0:
                    ans.append(ch)
                cnt += 1
            else:  # ')'
                cnt -= 1
                if cnt > 0:
                    ans.append(ch)
        return "".join(ans)