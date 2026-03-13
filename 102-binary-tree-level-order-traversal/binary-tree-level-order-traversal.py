from collections import deque

class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        q = deque([root])
        res = []

        while q:

            level = []
            size = len(q)

            for i in range(size):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res