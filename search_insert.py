class Solution():
	def searchInsert(self, List, target):
		F = 0
		L = len(List) - 1
		while F < L:
			M = (F + L) / 2
			if List[M] < target:
				F = M + 1
			else:
				L = M
		return F + 1 if List[F] < target else F



if __name__ == "__main__":
	inputList = [1,3,5,6]
	print Solution().searchInsert(inputList, 5)
	print Solution().searchInsert(inputList, 2)
	print Solution().searchInsert(inputList, 7)
	print Solution().searchInsert(inputList, 0)