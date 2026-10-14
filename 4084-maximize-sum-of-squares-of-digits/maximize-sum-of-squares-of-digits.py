class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > num * 9:
            return ""

        nines = sum // 9
        rem = sum % 9

        ans = "9" * nines

        if rem > 0:
            ans += str(rem)

        ans += "0" * (num - len(ans))

        return ans