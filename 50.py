class Solution:
	def findMin2(self, List):
		L = 0
		R = len(List) - 1
		while L < R and List[L] >= List[R]:
			M = (L + R) / 2
			if List[M] > List[R]:
				L = M + 1
			elif List[M] < List[L]:
				R = M
			else:
				L += 1
		return List[L]

if __name__ == "__main__":
	print Solution().findMin2([1,1,1,0,1])
	print Solution().findMin2([1,0,1,1,1])