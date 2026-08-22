class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        limit = len(nums) - 1 
        for num in range(limit):
            nums.append(nums[num])
        return nums