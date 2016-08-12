class Solution:
	# def balancedTree(self, root):
	# 	if not root:
	# 		return True
	# 	return abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1 //
	# 	and self.balancedTree(root.left) and self.balancedTree(root.right)

	# def treeHeight(self, root):
	# 	if not root:
	# 		return 0
	# 	return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))

	def balancedTree(self, root):
		return maxDepth(root) != 1
	def maxDepth(self, root):
		if not root:
			return 0
		L = maxDepth(root.left)
		if L == -1:
			return -1
		R = maxDepth(root.right)
		if R == -1:
			return -1
		return 1 + max(L, R) if abs(L - R) <= 1 else -1

