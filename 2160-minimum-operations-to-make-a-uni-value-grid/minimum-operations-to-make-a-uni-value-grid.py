class Solution:
    def minOperations(self, grid, x):
        
        arr = []
        
        for row in grid:
            arr.extend(row)
     
        base = arr[0]
        for num in arr:
            if (num - base) % x != 0:
                return -1
        arr.sort()
        median = arr[len(arr)//2]
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops