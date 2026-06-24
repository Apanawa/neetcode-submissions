class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in set:
                return False
            else:
                seen.add(num)
        return True