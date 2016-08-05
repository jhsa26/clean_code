'''
recursion way
'''
class Solution(object):
	def permute(self, nums):
		length = len(nums)
		res = []
		self.permuteHelper(nums, res, [], length)
		return res

	def permuteHelper(self, nums, res, temp, length):
		if len(temp) == length:
			res.append(temp)
		else:
			for i in range(len(nums)):
				self.permuteHelper(nums[:i] + nums[i + 1:], res, temp + [nums[i]], length)

'''
an interesting iterative way from the leetcode discuss
'''
class Solution:
	def permute(self, nums):
		perms = [[]]
		for n in nums:
			newperm = []
			for perm in perms:
				for i in range(len(perm) + 1):
					newperm.append(perm[:i] + [n] + perm[i:])
			perms = newperm
		return perms 
