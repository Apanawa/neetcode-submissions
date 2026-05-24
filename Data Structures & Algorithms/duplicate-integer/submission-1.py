class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        adan = False
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums[j]:
                    adan = True
                    return(adan)
        return adan

        

