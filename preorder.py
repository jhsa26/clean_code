class Solution:
	def preOrder(self, root, listt):
		stack = []
		while root or stack:
			if root:
				listt.append(root.val)
				root = root.left
				stack.append(root)
			else:
				root = stack.pop()
				root = root.right
		return listt