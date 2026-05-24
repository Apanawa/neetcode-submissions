class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s_clean += s[i].lower()
        l = 0
        r = len(s_clean)-1
        while l < r:
            if s_clean[l] != s_clean[r]:
                return False
            l += 1
            r -= 1
        return True