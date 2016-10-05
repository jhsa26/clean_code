class Solution:
	def reverse(self, s):
		results = s.split(None, -1)
		return " ".join(results[::-1])

if __name__ == "__main__":
	string = "the sky is blue"
	print Solution().reverse(string)