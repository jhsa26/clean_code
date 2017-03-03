'''
make place with 1 as 0 in the result matrix, 
for all others left, the algorithm is the
same as the uniquePathsI 
Time: O(m * n)
Space: O(m + n)
'''
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		result = [[0] * n for i in xrange(m)]
		for i in xrange(n):
			if obstacleGrid[0][i] == 1:
				break
			else:
				result[0][i] = 1
		for k in xrange(m):
			if obstacleGrid[k][0] == 1:
				break
			else:
				result[k][0] = 1
		for i in xrange(1, m):
			for j in xrange(1, n):
				if obstacleGrid[i][j] == 1:
					result[i][j] = 0
				else:
					result[i][j] = result[i-1][j] + result[i][j-1]
		return result[-1][-1]

'''
leetcode way which needs less Space
Time: O(m * n)
Space: O(min(m, n))
'''
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		result = [0] * n
		for i in xrange(n):
			if obstacleGrid[0][i] == 1:
				break
			else:
				result[i] = 1
		for j in xrange(1, m):
			if obstacleGrid[j][0] == 1:
				result[0] = 0

			for k in xrange(1, n):
				if obstacleGrid[j][k] == 1:
					result[k] = 0
				else:
					result[k] += result[k - 1]
		return result[n - 1]






