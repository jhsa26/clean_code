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
        self.dfs(candidates, target, res, [], 0)
        return res
    def dfs(self, candidates, target, res, temp, start):
        if target < 0:
            return
        elif target == 0:
            res.append(temp)
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                self.dfs(candidates, target - candidates[i], res, temp + [candidates[i]], i + 1)
print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
'''
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
'''




