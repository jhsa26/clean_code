class Solution:
	def atio(self, s):
		s = s.strip()
		sign = 1
		if s[0] == '-':
			sign = -1
			s = s[1:]
		elif s[0] == '+':
			s = s[1:]
		number = ''
		for i in range(len(s)):
			if s[i] >= '0' and s[i] <= '9':
				number += s[i]
			else:
				break
		if number == '':
			return 0
		if sign == 1 and int(number) > 2147483647:
			return 2147483647
		elif sign == -1 and int(number) > 2147483648:
			return -2147483648
		else:
			return sign * int(number)

if __name__ == "__main__":
	string = '  -21474836481234+1231234sd234fHsdf'
	print Solution().atio(string)