'''
similar way as N-Queens1
backtracking
'''
class Solution:
	def totalNQueens(self, n):
		count = 0
		self.totalNQueensHelper(n, count, [], range(n))
		return count
	def totalNQueensHelper(self, n, count, valueList, leftList):
		if len(valueList) == n:
			count += 1
		else:
			num = len(valueList)
			for i in range(len(leftList)):
				flag = 0
				for j in range(len(valueList)):
					if abs(valueList[j] - leftList[i]) == abs(j - num):
						flag = 1
				if flag == 0:
					self.totalNQueensHelper(n, count, valueList + [leftList[i]], leftList[:i] + leftList[i + 1:])
