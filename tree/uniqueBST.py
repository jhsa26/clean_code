'''
heapsort: space: O(nlog(n))
quicksort: quick but worst case if O(n^2) can deliberately used to cause security issue
mergesort: scalable O(nlog(n))
'''

'''
normally for division in python, if python 3 the '/' is the true division
'//' is the floor division
however if using the python2, then we can use "from __future__ import division" way
to make it work like python3
or we can also use way to coerce one of the operands as float like: 1/(2*1.0)
the 1/float(2) is also another work around, but since it can raise typeerror it's not that 
recommended.
math way: catalan number, for concrete proof, see wiki
Time: O(n)
Space: O(1)
'''
class Solution(object):
	def numTrees(self, n):
		if n == 0:
			return 1
		def combination(m, k):
			count = 1
			for i in range(1, k + 1):
				count = count * (m - i + 1) / i		
			return count
	### !!! here we have to use the other way around to avoid floor division
		return combination(2 * n, n) - combination(2 * n, n - 1) 

'''
一般来说求数量要首先想到dp问题， 如果像是下一题把所有树都例举出来 这时候就要用dfs来遍历所有的树了
normal DP way to deal with the problem
Time: O(n ^ 2)
Space: O(n)
'''
# class Solution(object):
# 	def numTrees(self, n):
# 		if n == 0:
# 			return 1
# 		count = 0
# 		for i in range(1, n + 1):
# 			count += self.numTrees(i - 1) * self.numTrees(n - i)
# 		return count
## the above way will cause the time exceed since the normal recursion does not
## have the advantage of memorization of dynamic programmming
# keep an array to list the dp list for the number of decisions, 
# dp[n] = dp[0] * dp[n - 1] + dp[1] * dp[n - 2] + ... + dp[n - 1] * dp[0]
class Solution(object):
	def numTrees(self, n):
		count = [1, 1, 2]
		if n <= 2:
			return count[n]
		else:
			count += [0 for i in range(n - 2)]
			for i in range(3, n + 1):
				for j in range(i):
					count += count[j] * count[i - 1 - j]
			return count[n]



