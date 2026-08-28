class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_appears = 0
        ans = {}
        res = 0
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1

        for key,value in ans.items():
            if value > max_appears:
                max_appears = value
                res = key

        return res
