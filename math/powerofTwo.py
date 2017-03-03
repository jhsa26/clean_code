def isPowerOfTwo(self, n):
	return n > 0 and 2 ** round(math.log(n, 2)) == n

def isPowerTwo(self, n):
	if n <= 0:
		return False
	if n == 1:
		return True
	if n % 2 == 1:
		return False
	return isPowerTwo(n / 2)