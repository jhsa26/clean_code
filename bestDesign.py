class Solution:
	def __init__(self, dic):
		self.dic = dic

	def add(self, number):
		if number in self.dic:
			self.dic[number] += 1
		else:
			self.dic[number] = 1

	def find(self, total):
		for item in self.dic:
			if item * 2 == total:
				if self.dic[item] >= 2:
					return True
			elif total - item in self.dic:
				return True
		return False

if __name__ == "__main__":
	a = Solution({})
	a.add(1)
	a.add(3)
	a.add(5)
	if a.find(50):
		print "True"
	else:
		print "False"
		print "haha"
	print a.dic
