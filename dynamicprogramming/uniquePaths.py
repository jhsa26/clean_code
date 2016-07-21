'''
my way is to use two dimensional array to record the ways to the destination
start from the first row and first column with 1 and others are 0
Time: O(m*n)
space: O(m*n)
'''

class Solution:
	def uniquePaths(self, m, n):
		ways = [[1] + [0] * (n-1) for i in range(m - 1)]
		firstline = [1] * n
		total = [firstline] + ways
		# import pdb
		# pdb.set_trace()
		for i in range(1, m):
			for j in range(1, n):
				total[i][j] = total[i-1][j] + total[i][j-1]
		return total[m-1][n-1]

if __name__ == '__main__':
	print Solution().uniquePaths(2, 3)
	print Solution().uniquePaths(3, 4)

'''
better way from the github Solution kind of wise
Time: O(m*n)
space: O(min(m + n))
'''

class Solution:
	def uniquePaths(self, m, n):
		if m < n:
			return self.uniquePaths(n, m)
		ways = [1] * n

		for i in xrange(1, m):
			for j in xrange(1, n):
				ways[j] += ways[j - 1]
		return ways[n - 1]



'''
math way to do this very smart!
use the formula:
C(N, k) = n!/(k!(n-k)!) = ((n - k + 1) * .. * n) / k !
Time: O(min(m , n))
Space: O(1)
'''
class Solution:
	def uniquePaths(self, m, n):
		N = m + n - 2
		k = m - 1  ## assume m < n
		res = 1
		for i in range(1, k + 1):
			res = res * (N - k + i) / i
		return res

