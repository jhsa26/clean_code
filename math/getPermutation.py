'''
this method is correct by exceed the time limit
'''
class Solution(object):
	def getPermutation(self, n, k):
		seq = range(1, n + 1)
		res = []
		self.helper(n, seq, res, [])
		return res[k - 1]

	def helper(self, n, seq, res, temp):
		if len(temp) == n:
			res.append(''.join(str(e) for e in temp))		## to convert a list of integer to string
		else:
			for i in range(len(seq)):
				self.helper(n, seq[:i] + seq[i + 1:], res, temp + [seq[i]])

if __name__ == '__main__':
	print Solution().getPermutation(3, 4)


