class Solution(object):
    def isValid(self, s):
        st=[]
        for ch in s:
            if(ch=='(' or ch=='{' or ch=='['):
                st.append(ch)
                continue
            if not st:
                return False
            if(ch==')'):
                if(st[-1]=='('):
                    st.pop()
                else:
                    return False
            elif(ch=='}'):
                if(st[-1]=='{'):
                    st.pop()
                else:
                    return False
            elif(ch==']'):
                if(st[-1]=='['):
                    st.pop()
                else:
                    return False
        return len(st) == 0
        