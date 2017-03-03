'''
make use of threeSum
and also pay attention to the point below
time: O(n ^ 3)
space: O(1), space is the extra space used in the progress and the returned space
'''
class Solution(object):
	def fourSum(self, nums, target):
		res = []
		nums.sort()
		for i in range(len(nums) - 3):
			if i and nums[i] == nums[i - 1]:
				continue		## important
			temp = self.threeSum(nums[i + 1:], target - nums[i])
			res = res + [[nums[i]] + item for item in temp]  ### use [nums[i]] instead of nums[i] here
		return res

	def threeSum(self, nums, target):
		newres = []
		nums.sort()
		for i in range(len(nums) - 2):
			if i and nums[i] == nums[i - 1]:
				continue		## important, similar to the while loop for j and k below
			j = i + 1
			k = len(nums) - 1
			while j < k:
				if nums[i] + nums[j] + nums[k] == target:
					newres.append([nums[i], nums[j], nums[k]])
					j += 1
					k -= 1
					while j < k and nums[j] == nums[j - 1]:
						j += 1
					while j < k and nums[k] == nums[k + 1]:
						k -= 1
				elif nums[i] + nums[j] + nums[k] < target:
					j += 1
				else:
					k -= 1
		return newres

if __name__ == '__main__':
	sample = [1, 2, 3, 4]
	print Solution().fourSum(sample, 10)
