'''
another way which is similar to the below method
since this time we make the decision inside and
also put the element directly into the helper function
without having to retrieve again, what's more we use
n-k + 2 to save more time this time.
'''
class Solution(object):
    def combine(self, n, k):
        return self.solve([], 1, [], n, k)

    def solve(self, ret, start, sofar, n, k):
        for i in range(start, n-k+2):
            if k == 1:
                ret.append(sofar+[i])
            else:
                self.solve(ret, i+1, sofar+[i], n, k-1)
        return ret


'''
previous method by me before, more formal way according
to the method taught in cs106b (will cause time exceed now?)
'''
class Solution(object):
	def combine(self, n, k):
		res = []
		self.combination(1, n, k, res, [])
		return res

	def combination(self, position, n, k, res, valueList):
		if len(valueList) == k:
			res.append(valueList[:])
			# the explanation here (valuelist[:] but not valuelist) is
			#
		for i in range(position, n + 1):
			valueList.append(i)
			self.combination(position + 1, n, k, res, valueList)
			valueList.pop()

if __name__ == '__main__':
	print Solution().combine(4, 2)




