class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        parentheses = []

        for char in s:
            if char == ")" and parentheses and parentheses[-1] == "(":
                parentheses.pop()
            elif char == "]" and parentheses and parentheses[-1] == "[":
                parentheses.pop()
            elif char == "}" and parentheses and parentheses[-1] == "{":
                parentheses.pop()
            else:
                parentheses.append(char)

        return len(parentheses) == 0