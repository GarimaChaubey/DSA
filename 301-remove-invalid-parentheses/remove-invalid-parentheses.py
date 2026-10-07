class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = set([s])

        while queue:

            result = []

            for curr in queue:
                if isValid(curr):
                    result.append(curr)

            if result:
                return result

            next_level = []

            for curr in queue:

                for i in range(len(curr)):

                    if curr[i] not in '()':
                        continue

                    if i > 0 and curr[i] == curr[i - 1]:
                        continue

                    new_string = curr[:i] + curr[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            queue = next_level

        return [""]
        