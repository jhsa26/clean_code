'''
if wanna change certain character in string:
1st way:
test = 'abcd'
new = list(test)
new[2] = 'Q'
''.join(new)
2rd way:
test = 'abc'
test = test[:2] + 'Q' + test[3:]
'''

class Solution(object):
	def solveNQueens(self, n):
		res = []
		options = []
		for i in range(n):			## string is not mutable in python
			string = '.' * i + 'Q' + '.' * (n - i - 1)
			options.append(string)
		self.solveNQueensHelper(n, res, options, [], range(n))
		return res

	def solveNQueensHelper(self, n, res, options, valueList, leftList):
		if len(valueList) == n:
			res.append([options[i] for i in valueList])
		else:
			num = len(valueList)
			for j in range(len(leftList)):
				flag = 0
				for m in range(len(valueList)):
					if abs(leftList[j] - valueList[m]) == abs(num - m):
						flag = 1
				if flag == 0:
					self.solveNQueensHelper(n, res, options, valueList + [leftList[j]], leftList[:j] + leftList[j + 1:])







