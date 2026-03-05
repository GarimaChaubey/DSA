# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        k = k % cnt

        if k==0:
            return head

        temp=head
        for i in range(cnt-k-1):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        tail = newhead
        while tail.next:
            tail = tail.next

        tail.next = head
        return newhead 
        
        