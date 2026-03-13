class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):

        def can(time):
            total = 0

            for t in workerTimes:

                left, right = 0, mountainHeight

                while left <= right:
                    mid = (left + right) // 2

                    if t * mid * (mid + 1) // 2 <= time:
                        left = mid + 1
                    else:
                        right = mid - 1

                total += right

                if total >= mountainHeight:
                    return True

            return False


        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        ans = right

        while left <= right:

            mid = (left + right) // 2

            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans