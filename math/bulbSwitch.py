'''
just to calculate the number of full squares along
the way
'''
class Solution(object):
	def bulbSwitch(self, n):
		if n == 0:
			return 0
		i = 1
		while True:
			if i ** 2 <= n and (i + 1) ** 2 > n:
				return i
			else:
				i = i + 1
import math
class Solution(object):
	def bulbSwitch(self, n):
		return int(math.sqrt(n))


if __name__ == '__main__':
	print Solution().bulbSwitch(1)
	print Solution().bulbSwitch(9)