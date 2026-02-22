class Solution(object):
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)

        low= min(bloomDay)
        high=max(bloomDay)
        #ans=high
        if(n<(m*k)):
            return -1

        def make(day):
            bouquet=0
            flower=0

            for bloom in bloomDay:
                if bloom<=day:
                    flower+=1
                    if flower==k:
                        bouquet+=1
                        flower=0
                else:
                    flower=0
            return bouquet>=m
        while(low<=high):
            mid=(low+high)//2

            if make(mid):
                high=mid-1
            else:
                low=mid+1
        return low


        