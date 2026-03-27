class Solution:
    def areSimilar(self, mat, k):
        
        m, n = len(mat), len(mat[0])
        
        shift = k % n
        
        for i in range(m):
            row = mat[i]
            
            if i % 2 == 0:
                # left shift
                new_row = row[shift:] + row[:shift]
            else:
                # right shift
                new_row = row[-shift:] + row[:-shift]
            
            if new_row != row:
                return False
        
        return True