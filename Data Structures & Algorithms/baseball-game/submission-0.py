class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for op in range(len(operations)):
            if operations[op] == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif operations[op] == "D":
                stack.append(int(stack[-1]) * 2)
            elif operations[op] == "C":
                stack.pop()
            else:
                stack.append(int(operations[op]))
        
        print(stack)
        ans = 0
        for num in range(len(stack)):
            ans += stack[num]
        return ans