# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        curr = root
        
        while curr:
            # If there's a left child, we need to move it
            if curr.left:
                # 1. Find the rightmost node in the left subtree
                last = curr.left
                while last.right:
                    last = last.right
                
                # 2. Connect current's right child to the right of 'last'
                last.right = curr.right
                
                # 3. Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # 4. Move to the next node on the right
            curr = curr.right