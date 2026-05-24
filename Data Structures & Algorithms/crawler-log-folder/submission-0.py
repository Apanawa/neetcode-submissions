class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in range(len(logs)):
            if logs[log] == "../" and len(stack) > 0:
                stack.pop()
            elif logs[log] != "./" and logs[log] != "../":
                stack.append(logs[log])

        return(len(stack))
            