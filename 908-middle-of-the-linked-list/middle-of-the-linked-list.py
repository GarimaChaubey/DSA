# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        cnt=0
        temp=head
        while temp:
            temp=temp.next
            cnt+=1

        middle_node=(cnt//2)
        temp=head
        for i in range(middle_node):
            temp=temp.next
        return temp