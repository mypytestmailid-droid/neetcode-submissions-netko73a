class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #initiate dictionary to count number of chars
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1
        return all( v == 0 for v in counts.values())   
        
obj = Solution()
