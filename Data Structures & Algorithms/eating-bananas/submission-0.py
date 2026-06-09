class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            time = 0

            for pile in piles:
                time += (pile + mid - 1) // mid

            if time <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo