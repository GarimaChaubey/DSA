
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = [-1] * n
        last = [-1] * 26

        stack = [(0, 1, -1)]

        while stack:
            node, entering, old = stack.pop()
            c = ord(s[node]) - ord('a')

            if entering == 1:
                old = last[c]

                if node == 0:
                    new_parent[node] = -1
                elif old != -1:
                    new_parent[node] = old
                else:
                    new_parent[node] = parent[node]

                last[c] = node

                stack.append((node, 0, old))

                for child in reversed(children[node]):
                    stack.append((child, 1, -1))

            else:
                last[c] = old

        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            p = new_parent[node]
            new_children[p].append(node)

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        ans = [1] * n

        for node in reversed(order):
            p = new_parent[node]

            if p != -1:
                ans[p] += ans[node]

        return ans
