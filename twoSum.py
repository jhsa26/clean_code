class Solution:
	def two_sum(self, array, total):
		res = {}
		for i, item in enumerate(array):
			if total - item in res:
				return i, res[total - item]
			res[item] = i
		return None

if __name__ == "__main__":	
	array = [3,6,1,7,8,90]
	total = 93
	print Solution().two_sum(array, total)