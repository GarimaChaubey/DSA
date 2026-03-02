class Solution(object):
    def frequencySort(self, s):
        freq={}

        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        sorted_item = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result=""

        for ch, counts in sorted_item:
            result+=ch*counts
        
        return result