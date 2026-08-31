class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            nxt = curr.next

            # Check if current node is a critical point
            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    minDist = min(minDist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Less than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        return [minDist, last - first]