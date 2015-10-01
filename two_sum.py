class Solution:
	def two_sum(self, array, total):
		res = {}
		for index, item in enumerate(array):
			res[item] = index + 1
		for item in array:
			if total - item in res:
				return res[item], res[total - item]
		return None

if __name__ == "__main__":	
	array = [3,6,1,7,8,90]
	total = 93
	print Solution().two_sum(array, total)