class Solution:
	# def minDepth(self, root):
	# 	if root is None:
	# 		return 0
	# 	elif root.left is None:
	# 		return 1 + self.minDepth(root.right)
	# 	elif root.right is None:
	# 		return 1 + self.minDepth(root.left)
	# 	else:
	# 		return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
	def minDepth(self, root):
		if root is None:
			return 0
		neighbors = []
		neighbors.append(root)
		length = 1
		end = root
		while neighbors:
			check = neighbors.pop()
			if check.left is not None:
				neighbors.append(neighbors.left)
			if check.right is not None:
				neighbors.append(neighbors.right)
			if not check.left or not check.right:
				break
			if check is end:
				length += 1
				end = check.right is check.right is not None else check.left
		return length


