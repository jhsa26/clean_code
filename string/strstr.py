class Solution:
	def strStr(self, haystack, needle):
		len1 = len(haystack)
		len2 = len(needle)
		if len1 < len2:
			return -1
		for i in range(len1):
			if i + len2 <= len1:
				if haystack[i:i+ len1] == needle:
					return i
			else:
				return -1
		if len2 == 0:
			return 0
		else:
			return -1

if __name__ == "__main__":
	print Solution().strStr("aaba", "ba")