class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_appears = {}
        ans = 0
        for num in nums:
            if num in nums_appears:
                nums_appears[num] += 1
            else:
                nums_appears[num] = 1
        ans = max(nums_appears, key=nums_appears.get)
        return ans

