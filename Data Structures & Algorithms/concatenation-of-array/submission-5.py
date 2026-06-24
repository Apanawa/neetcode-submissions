class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = len(nums)
        while j < i:
            nums.append(nums[j])
            j += 1
        return nums
