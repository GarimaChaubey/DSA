# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        st=[]
        temp=head
        while temp:
            st.append(temp.val)
            temp=temp.next
        
        temp=head
        while temp:
            if(st.pop()!=temp.val):
                return False
            temp=temp.next
        return True
        