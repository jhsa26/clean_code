class Solution:
	def inOrder(self, root, list1):
		stack = []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				list1.append(root.val)
				root = root.right
		return list1