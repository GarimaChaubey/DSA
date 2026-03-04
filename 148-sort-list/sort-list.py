# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        st=[]
        temp=head
        while temp:
            st.append(temp.val)
            temp=temp.next
        st.sort()
        temp=head
        i=0
        while temp:
            temp.val=st[i]
            i+=1
            temp=temp.next
        return head