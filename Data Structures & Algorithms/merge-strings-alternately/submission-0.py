class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        character = 0

        if len(word1) > len(word2):
            count = len(word2)
            temp = True
        else:
            count = len(word1)
            temp = False
        
        while character < count:
            ans += word1[character]
            ans += word2[character]
            character += 1
        
        if temp == True:
            while character < len(word1):
                ans += word1[character]
                character += 1
        else:
            while character < len(word2):
                ans += word2[character]
                character += 1
        return ans