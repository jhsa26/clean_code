'''
use len(x) == len(set(x)) way to determine if duplication
use brute force way to check the validation overall
solution given by github fork
time complexity O(n^2)
space O(n)
'''
class Solution:
	def isValidSudoku(self, board):
		for i in range(9):
			if not self.lineValid(board[i]) or not self.lineValid([board[j][i] for j in range(9)]):
				return False
		for m in range(3):
			for n in range(3):
				if not self.lineValid([board[i][j] for i in range(3 * m, 3 * m + 3) for j in range(3 * n, 3 * n + 3)]):
					return False
		return True

	def lineValid(self, xs):
		xs = filter(lambda x: x != '.', xs)
		return len(xs) == len(set(xs))


'''
use different set() to track the duplication
use math way (put the grid in one row) to check the grid validation
solution given by jiuzhang
time complexity O(n^2)
space complexity O(n)
'''
class Solution:
	def isValidSudoku(self, board):
		rowSet = [set() for i in range(9)]
		colSet = [set() for i in range(9)]
		gridSet = [set() for i in range(9)]

		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					continue
				elif board[i][j] in rowSet[i] or board[i][j] in colSet[j]:
					return False

				k = i / 3 * 3 + j / 3
				if board[i][j] in gridSet[k]:
					return False

				rowSet[i].add(board[i][j])
				colSet[j].add(board[i][j])
				gridSet[k].add(board[i][j])
		return True




