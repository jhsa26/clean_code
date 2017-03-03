class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        last, i = 0, 1
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
            i += 1
        return last + 1

print Solution().removeDuplicates([1, 2, 2, 3, 5, 5, 5])

'''
time: O(n)
space: O(1)
follow the normal mind for keeping the unique values
'''
