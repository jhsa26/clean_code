class Solution:
	def singleNumber(self, A):
		total = 0
		for i in A:
			total = total ^ i
		return total

if __name__ == "__main__":
	A = [2,3,4,4,2]
	print Solution().singleNumber(A)

total = total ^ a
total = total | a
total = total & a
~ total
total << 1
total >> 1