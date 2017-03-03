'''
pay attention to the difference between
the power of three and three to the power of what...
first way is to use logarithm, to see if the rounded one
it the same as the result
the second method is to use recursive way
 '''
class Solution(object):
	def isPowerOfThree(self, n):
		return n > 0 and 3 ** round(math.log(n, 3)) == n

class Solution(object):
	def isPowerOfThree(self, n):
		if n < 0:
			return False
		if n == 1:
			return True
		if n == 0 or n % 3 > 0:      ### pay attention to the condition here
			return False
		return self.isPowerOfThree(n / 3)

if __name__ == '__main__':
	print Solution().isPowerOfThree(27)
		