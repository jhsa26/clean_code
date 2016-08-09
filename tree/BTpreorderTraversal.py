'''
recursion
Time: O(n)
space: O(h)
'''
class Solution(object):
	def preorderTraversal(self, root):
		if not root:
			return []   ## here is [] not None
		return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)



'''
iteration
Time: O(n)
space: O(h)
'''
class Solution(object):
	def preorderTraversal(self, root):
		result, stack = [], [(root, False)]
		while stack:
			cur, visited = stack.pop()
			if cur:
				if visited:
					result.append(cur.val)
				else:
					stack.append((cur.right, False))
					stack.append((cur.left, False))
					stack.append((cur, True))
		return result