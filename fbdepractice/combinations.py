'''
def combine(self, n, k):
	res = []
	self.dfs(range(1, n + 1), k, [], res)
	return res

def dfs(self, nums, k, path, res):
	if k == 0:
		res.append(path)
		return
	if len(nums) >= k:
		for i in range(len(nums)):
			self.dfs(nums[i + 1:], k - 1, path + [nums[i]], res)
	return

if __name__ == '__main__':
	print Solution().combine(4, 2)
'''

## more traditional and easy understood way
'''
Time: O(n!)
Space: O(n)
'''
class Solution:
    def combine(self, n, k):
        result = []
        self.dfs(n, result, 0, [], k)
        return result
    def dfs(self, n, result, start, temp, k):
        if k == len(temp):
            result.append(temp) # when using  temp.append, temp.add() way to do backtracking, we have to pass a copy like [:], but when directly pass the list into the recursive function, we do not have to
            return
        for i in range(start, n):
           # temp.append(i + 1)
            self.dfs(n, result, i + 1, temp + [i + 1], k)
           # temp.pop()

if __name__ == "__main__":
    result = Solution().combine(4, 2)
    print result


