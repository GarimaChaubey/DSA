class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x1 = max(rec1[0], rec2[0])
        x2 = min(rec1[2], rec2[2])

        y1 = max(rec1[1], rec2[1])
        y2 = min(rec1[3], rec2[3])

        return x2 > x1 and y2 > y1
        