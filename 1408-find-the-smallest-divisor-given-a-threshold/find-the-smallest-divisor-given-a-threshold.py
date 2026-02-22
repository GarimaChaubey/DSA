class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
       
        n=len(nums)
        def canmake(divisor):
            sum=0
            for num in nums:
                
                sum += (num + divisor - 1)// divisor
            return sum<=threshold

        while(low<=high):
            mid=(low+high)//2
            if(canmake(mid)):
                
                high=mid-1
            else:
                low=mid+1
        return low


        