'''
first we should use normal human brain to mimic the way for the algorithm
then to see if it's applicable to computer,
last implement what the thinking process in a proper laguage code
'''
## recursive way
class Solution:
	def permuteUnique(self, nums):
		length = len(nums)
		res = []
		self.permuteUniqueHelper(nums, res, [], length)
		return res

	def permuteUniqueHelper(self, nums, res, valueList, length):
		if len(valueList) == length:
			res.append(valueList)
		else:
			used = []
			for i in range(len(nums)):
				if nums[i] not in used:
					self.permuteUniqueHelper(nums[:i] + nums[i + 1:], res, valueList + [nums[i]], length)
					used.append(nums[i])


## interative way by leetcode
class Solution:
	def permuteUnique(self, nums):
		solutions = [[]]
		for num in nums:
			next = []
			for solution in solutions:
				for i in range(len(solution) + 1):
					newlist = solution[:i] + [num] + solution[i:]
					if newlist not in next:
						next.append(newlist)
			solutions = next
		return solutions
