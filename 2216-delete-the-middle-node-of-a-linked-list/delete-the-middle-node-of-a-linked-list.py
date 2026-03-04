# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        
        temp=head
        for i in range(cnt//2-1):
            temp=temp.next
        temp.next=temp.next.next

        return head
            
        