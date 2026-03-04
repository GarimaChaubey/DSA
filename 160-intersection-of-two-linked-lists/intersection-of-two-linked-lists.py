class Solution(object):
    def getIntersectionNode(self, headA, headB):

        visited = set()
        temp = headA

        # store nodes of list A
        while temp:
            visited.add(temp)
            temp = temp.next

        temp = headB

        # check nodes of list B
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None