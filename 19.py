class Solution:
	def panlidromeNumber(self, num):
		if num < 0:
			return False
		copy, rev = num, 0
		while True:
			rev *= 10
			low = num % 10
			rev += low
			num = num / 10
			if num == 0:
				break
		return rev == copy

if __name__ == "__main__":
	number = 12343
	print Solution().panlidromeNumber(number)
