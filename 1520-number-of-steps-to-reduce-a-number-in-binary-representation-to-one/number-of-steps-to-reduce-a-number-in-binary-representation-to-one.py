class Solution(object):
    def numSteps(self, s):

        steps = 0
        carry = 0

        # process from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):

            bit = int(s[i])

            if bit + carry == 1:
                # odd case
                steps += 2
                carry = 1
            else:
                # even case
                steps += 1

        # if carry remains, one extra step
        return steps + carry