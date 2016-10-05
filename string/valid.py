class Solution:
	def valid(self, s):
		s = s.strip()
		if s[0] in ['+', '-']:
			s = s[1:]
		for i in range(len(s)):
			if s[i] >= '0' and s[i] <= '9':
				continue
			elif s[i] == '.':
				if len(s) == 1 or not self.truenumber(s[i + 1:]):
					return False
			else:
				return False
		return True

	def truenumber(self, s):
		for i in range(len(s)):
			if s[i] >= '0' and s[i] <= '9':
				continue
			else:
				return False
		return True

if __name__ == "__main__":
	s = '  +1234.1111SDF234'
	print Solution().valid(s)
