class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        ans = 0

        for i in range(n):

            cnt = 0

            for j in range(i, n):

                if nums[j] == target:
                    cnt += 1

                length = j - i + 1

                if cnt > length // 2:
                    ans += 1

        return ans