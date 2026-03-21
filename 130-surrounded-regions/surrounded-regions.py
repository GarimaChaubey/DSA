class Solution:
    def solve(self, board):
        
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'  # mark safe
            
            # explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Step 1: mark boundary connected O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # Step 2: flip surrounded + restore safe
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'