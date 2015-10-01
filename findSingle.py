class Solution:
	def findSingle(self, res):
		num = 0
		for item in res:
			num ^= item
		return num
	def findSingle1(self, res):
		dic = {}
		for item in res:
			if item in dic:
				dic[item] += 1
			else:
				dic[item] = 1
		for i, j in dic.items():
			if j == 1:
				return i
	def findSingle2(self, res):
		a = set()
		for item in res:
			if item in a:
				a.remove(item)
			else:
				a.add(item)
		return a.pop()

if __name__ == "__main__":
	res = [2,4,3,5,4,3,2,5,7]
	print Solution().findSingle(res)
	print Solution().findSingle1(res)
	print Solution().findSingle2(res)