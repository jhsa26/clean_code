class Solution:
	def reverseString(self, s):
		s = s[::-1]
		result = s.split(" ")
		alter = map(lambda x : x[::-1], result)
		return " ".join(alter)



if __name__ == "__main__":
	string = "I love women"
	print Solution().reverseString(string)
	# print Solution().trueReverse(string)