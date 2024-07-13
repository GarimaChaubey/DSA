#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # code here 
        if n == int(str(n)[::-1]):
            return n
        
        for i in range(0, 5):
            ad = int(str(n)) + int(str(n)[::-1])
            if ad == int(str(ad)[::-1]):
                return ad
            n = ad
        return '-1'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends