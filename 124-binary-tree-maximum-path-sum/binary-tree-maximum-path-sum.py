class Solution(object):
    def maxPathSum(self, root):

        self.sum = float('-inf')

        def height(node):

            if not node:
                return 0

            leftsum = max(0, height(node.left))
            rightsum = max(0, height(node.right))

            self.sum = max(self.sum, leftsum + rightsum + node.val)

            return node.val + max(leftsum, rightsum)

        height(root)

        return self.sum