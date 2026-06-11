class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0

        for price in prices:
            minPrice = min(minPrice, price)
            ans = max(ans, price - minPrice)

        return ans