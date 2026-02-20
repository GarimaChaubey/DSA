class Solution(object):
    def makeLargestSpecial(self, s):
        # Base case
        if len(s) <= 2:
            return s

        count = 0
        start = 0
        blocks = []

        # Step 1: split into top-level special blocks
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            # When balance becomes 0, one full block found
            if count == 0:
                # Recursively process inside part
                inner = self.makeLargestSpecial(s[start+1:i])
                blocks.append("1" + inner + "0")
                start = i + 1

        # Step 2: sort blocks in descending order
        blocks.sort(reverse=True)

        # Step 3: join them
        return "".join(blocks)
        