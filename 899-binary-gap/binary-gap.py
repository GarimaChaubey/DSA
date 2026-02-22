class Solution(object):
    def binaryGap(self, n):

        prev = -1
        result = 0
        position = 0

        while n > 0:

            if n & 1:   # check last bit
                if prev != -1:
                    result = max(result, position - prev)
                prev = position

            n >>= 1     # right shift
            position += 1

        return result
