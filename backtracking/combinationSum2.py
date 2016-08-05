'''
This version I will check the duplicate after collect all the result, the latter version will cut the 
result more earlier which will save more time compared to this
Compared to combinationSum1, this is a collection instead of a set and every number can only appear once
Time: 


'''
class Solution(object):
	def combinationSum2(self, candidates, target):
		candidates.sort()
		res = []
		valueList = []
		self.combinationSum2Helper(candidates, target, res, valueList, 0)
		return res

	def combinationSum2Helper(self, candidates, target, res, valueList, index):
		length = len(candidates)
		if target == 0 and valueList not in res:
			res.append(valueList)
		else:
			for i in range(index, length):
				if candidates[i] > target:
					return
				else:
					self.combinationSum2Helper(candidates, target - candidates[i], res, valueList + [candidates[i]], i)


class Solution:
	def combinationSum2(self, candidates, target):
		candidates.sort()
		res = []
		self.combinationSum2Helper(candidates, res, 0, [], target)
		return res

	def combinationSum2Helper(self, candidates, res, index, valueList, target):
		if target == 0:
			res.append(valueList)
		prev = 0
		while index < len(candidates) and candidates[index] <= target:
			if prev != candidates[index]:
				self.combinationSum2Helper(candidates, res, index + 1, valueList + [candidates[index]], target - candidates[index])
				prev = candidates[index]
			index += 1





