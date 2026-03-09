class Solution(object):
    def largestRectangleArea(self, heights):

        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):

            cur = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > cur:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area