from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        rows=len(mat)
        cols=len(mat[0])
        q=deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float('inf')

        dirs=[(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c=q.popleft()

            for dr, dc in dirs:
                nr=r+dr
                nc=c+dc

                if 0<=nr<rows and 0<=nc<cols:
                    if mat[nr][nc]>mat[r][c]+1:
                        mat[nr][nc]=mat[r][c]+1
                        q.append((nr,nc))

        return mat