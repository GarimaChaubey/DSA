class Solution(object):
    def numSpecial(self, mat):
        m=len(mat)
        n=len(mat[0])

        rows=[0]*m
        col=[0]*n
        cnt=0

        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1):
                    rows[i]+=1
                    col[j]+=1
        
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1 and rows[i]==1 and col[j]==1):
                    cnt+=1
        return cnt
                
