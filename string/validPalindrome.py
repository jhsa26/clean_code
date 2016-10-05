class Solution:
	def valid(self, s):
		start = 0
		end = len(s) - 1
		while start < end:
			while start < end and not s[start].isalnum():
				start += 1
			while start < end and not s[end].isalnum():
				end -= 1
			if s[start].lower() != s[end].lower():
				return False
			else:
				start += 1
				end -= 1
		return True

if __name__ == "__main__":
	if Solution().valid('A man, a plan, a canal: Panama'):
		print "wow"
	else:
		print "bad"