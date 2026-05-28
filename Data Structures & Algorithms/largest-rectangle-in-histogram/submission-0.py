class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights.append(0)  # fuerza a vaciar el stack al final
        stack = []         # guardamos índices

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                height = heights[stack[-1]]
                stack.pop()

                left = stack[-1] if stack else -1
                width = i - left - 1

                ans = max(ans, width * height)

            stack.append(i)

        heights.pop()  # opcional: deja la lista como estaba
        return ans