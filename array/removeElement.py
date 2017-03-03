'''
pay attention to the remove in place
and the index problem covering the edge case here
do not use built-in functions that easily when
in place or cerain time complexity is a requirement

delete multiple indexes from a list in python:
    example: a = [1, 2, 5, 5, 6 ,7]
    ind2remove = [2, 5, 3]
    1. put the index in reverse order:
    for i in sorted(ind2remove, reverse = True):
        del a[i]
    2. use list comprehension
    a = [x for i, x in enumerate(a) if i not in ind2remove]
    3. use numpy
    import numpy as np
    a = np.array(a)
    print np.delete(a, ind2remove)
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return end + 1
