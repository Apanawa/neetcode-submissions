class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = len(nums)
        while i > 0:
            nums.append(nums[i])
            i -= 1
        return nums
