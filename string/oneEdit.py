class Solution:
	def oneEdit(self, s, t):
		m = len(s)
		n = len(t)
		if abs(m - n) > 1:
			return False
		if m > n:
			return self.oneEdit(t, s)
		for i in range(m):
			if s[i] != t[i]:
				if m < n:
					return s[i:] == t[i + 1:]
				if m == n:
					return s[i + 1:] == t[i + 1:]
		return True

if __name__ == "__main__":
	s = "abcd"
	t = "abxd"
	t1 = "abcde"
	t2 = "abcfd"
	t3 = "asfdf"
	if Solution().oneEdit(s,t):
		print "t"
	if Solution().oneEdit(s,t1):
		print "t1"
	if Solution().oneEdit(s,t2):
		print "t2"
	if Solution().oneEdit(s,t3):
		print "t3"