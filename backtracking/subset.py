'''
class Solution(object):
    def subsets(self, nums):
        results = []
       # nums.sort()
        self.dfs(results, nums, [], 0)
        return results

    def dfs(self, res, nums, temp, start):
        res.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.dfs(res, nums, temp, i + 1)
            temp.pop()

print Solution().subsets([1, 2, 3])
'''

## because python's syntax, it's not neccessary to pass start parameter and backtrack manually for temp list:

class Solution(object):
    def subset(self, nums):
        results = []
        self.dfs(results, nums, [])
        return results
    def dfs(self, res, nums, temp):
        res.append(temp[:])
        for i in range(len(nums)):
            self.dfs(res, nums[i + 1:], temp + [nums[i]])

print Solution().subset([1, 2, 3])
