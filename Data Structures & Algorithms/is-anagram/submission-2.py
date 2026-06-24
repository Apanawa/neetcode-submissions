class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in char_s:
                char_s[c] = 1
            else:   
                char_s[c] += 1
        for c in t:
            if c not in char_t:
                char_t[c] = 1
            else:   
                char_t[c] += 1        
        return char_s == char_t