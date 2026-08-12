class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if num == ans:
                count += 1
            else:
                count -= 1

        return ans

        """
        ans = 1
        count = 1
        num = 2
        [1,2,3,2,2,2,5,4,2]
           n
        """