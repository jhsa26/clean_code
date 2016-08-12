class Solution:
	# def arrayToBST(self, array):
	# 	if not array:
	# 		return None
	# 	length = len(array)
	# 	newNode = TreeNode(array[length/2])
	# 	newNode.left = self.arrayToBST(array[:length/2])
	# 	newNode.right = self.arrayToBST(array[length/2 + 1 :])
	# 	return newNode
	def arrayToBST(self, array):
		if not array:
			return None
		return self.createBST(array, 0, len(array) - 1)

	def createBST(self, array, start, end):
		if start > end:
			return None
		mid = (start + end) / 2
		newNode = TreeNode(array[mid])
		newNode.left = self.createBST(array, start, mid - 1)
		newNode.right = self.createBST(array, mid + 1, end)
		return newNode


