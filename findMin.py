class Solution:
	def findMin(self, List):
		L = 0
		R = len(List) - 1
		while L < R and List[L] > List[R]:
			M = (L + R) / 2
			if List[M] > List[R]:
				L = M + 1
			else:
				R = M
		return List[L]

if __name__ == "__main__":
	print Solution().findMin([4,5,6,7,0,1,2])