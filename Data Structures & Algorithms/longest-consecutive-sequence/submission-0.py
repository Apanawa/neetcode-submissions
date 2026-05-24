class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        ans = 0

        for num in my_set:
            if num - 1 not in my_set:
                count = 1
                while num + count in my_set:
                    count += 1
                if count > ans:
                    ans = count
                count = 0
        return ans
                
        