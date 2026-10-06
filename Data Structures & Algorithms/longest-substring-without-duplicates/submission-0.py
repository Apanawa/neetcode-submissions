class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "pwwkew"
         l
         r
        set = 
        lon = 
        """
        chars = set()
        lon_sub = 0
        l = 0
        r = 0
        # chars.add(s[l])
        while r < len(s):
            """
            if s[l] in chars:
                r += 1
            else:
                chars.add(s[l])
            """
            if s[r] in chars:
                chars.remove(s[l])
                l += 1  
            else:
                chars.add(s[r])
                r += 1
            lon_sub = max(len(chars), lon_sub)
        return lon_sub