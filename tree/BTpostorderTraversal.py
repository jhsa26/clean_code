'''
recursion
Time: O(n)
Space: O(h)
'''
class Solution(object):
	def postorderTraversal(self, root):
		if not root:
			return []
		return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

'''
iteration
Time: O(n)
Space: O(h)
'''
class Solution(object):
	def postorderTraversal(self, root):
		result, stack = [], [(root, False)]
		while stack:
			cur, visited = stack.pop()
			if cur:
				if visited:
					result.append(cur.val)
				else:
					stack.append((cur, True))
					stack.append((cur.right, False))
					stack.append((cur.left, False))
		return result