class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:   # pay attention to here
            mid = l + (r - l) / 2
            if target == nums[mid]:
                return mid
            if nums[l] < nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

print Solution().search([4, 5, 6, 7, 0, 1, 2], 6)

