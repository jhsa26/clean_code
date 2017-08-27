class Solution(object):
    def subsetWithDup(self, nums):
        results = []
        nums.sort()  # not like subset.py, need to sort here in order to filter out the duplicates by conditions below
        self.dfs(results, nums, [], 0)
        return results
    def dfs(self, results, nums, temp, start):
        results.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(results, nums, temp + [nums[i]], i + 1)


print Solution().subsetWithDup([1, 2, 2])
