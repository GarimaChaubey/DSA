# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):

        visited = {}
        temp = head

        while temp:
            if temp in visited:
                return True

            visited[temp] = True
            temp = temp.next

        return False
        