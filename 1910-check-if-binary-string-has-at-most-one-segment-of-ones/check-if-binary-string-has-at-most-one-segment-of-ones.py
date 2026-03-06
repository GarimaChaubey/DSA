class Solution(object):
    def checkOnesSegment(self, s):

        seen_zero = False

        for ch in s:

            if ch == '0':
                seen_zero = True

            if ch == '1' and seen_zero:
                return False

        return True