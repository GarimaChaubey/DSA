class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            x = nums[i]
            sum = 0

            while x > 0:
                sum += x % 10
                x //= 10

            if sum == i:
                return i

        return -1
        