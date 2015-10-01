class Solution:
	def stairs(self, n):
		i, j = 1, 1
		for k in range(n - 1):
			i, j = j, i + j
		return j

if __name__ == "__main__":
	print Solution().stairs(5)