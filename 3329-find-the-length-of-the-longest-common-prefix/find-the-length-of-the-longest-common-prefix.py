class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        st = set()

        # Step 1: store prefixes of arr1
        for num in arr1:
            while num > 0:
                st.add(num)
                num //= 10

        max_len = 0

        # Step 2: check prefixes of arr2
        for num in arr2:
            while num > 0:
                if num in st:
                    max_len = max(max_len, len(str(num)))
                    break
                num //= 10

        return max_len