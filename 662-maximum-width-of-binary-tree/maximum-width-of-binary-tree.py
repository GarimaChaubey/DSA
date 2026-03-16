from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):

        q = deque([(root,0)])
        ans = 0

        while q:

            size = len(q)

            first_index = q[0][1]
            last_index = q[-1][1]

            ans = max(ans, last_index - first_index + 1)

            for _ in range(size):

                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2*idx))

                if node.right:
                    q.append((node.right, 2*idx+1))

        return ans