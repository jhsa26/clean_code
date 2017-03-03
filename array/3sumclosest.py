'''
similar to 3sum, only to find one closest is enough
time:O(n^2)
space: O(1)
'''
class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		result = nums[0] + nums[1] + nums[2]
		for i in range(len(nums) - 2):
			if i and nums[i] == nums[i - 1]:
				continue
			j = i + 1
			k = len(nums) - 1
			while j < k:
				total = nums[i] + nums[j] + nums[k] 
				print total
				if total == target:
					return target
				if abs(total - target) < abs(result - target):
					result = total
				if total > target:
					k -= 1
				if total < target:
					j += 1
		return result

if __name__ == '__main__':
	print Solution().threeSumClosest([1, 1, 1, 0], 100)