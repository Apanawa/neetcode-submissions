class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for num in tokens:
            if num == "+":
                s.append(s.pop() + s.pop())
            elif num == "*":
                s.append(s.pop() * s.pop())
            elif num == "/":
                x = s.pop()
                y = s.pop()
                s.append(int(float(y) / x))
            elif num == "-":
                x = s.pop()
                y = s.pop()
                s.append(y - x)
            else:
                s.append(int(num))
        return s[0]