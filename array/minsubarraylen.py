class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, result = 0, 0
        size = len(nums) + 1
        for right, i in enumerate(nums):
            result += i
            while result >= s:
                size = min(size, right - left + 1)
                result -= nums[left]
                left += 1
        return 0 if size > len(nums) else size
