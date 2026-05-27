class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0
        while (l < r ):
            maxWater = max(maxWater, (r-l) * min(height[l],height[r]))
            if (height[l] < height[r]):
                l += 1
            elif (height[l] == height[r]):
                if height[l] > height[r-1]:
                    r -= 1
                else:
                    l += 1
            else:
                r -= 1
        return maxWater