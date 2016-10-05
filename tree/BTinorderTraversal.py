'''
recursion
Time: O(n)
Space: O(h)
'''
class Solution(object):
	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
		return res


'''
iteration
use a visited flag to facilitate the process
Time: O(n)
Space: O(h)
'''
class Solution(object):
	def inorderTraversal(self, root):
		result, stack = [], [(root, False)]
		while stack:
			cur, visited = stack.pop()
			if cur:     ## remember to check cur
				if visited:
					result.append(cur.val)
				else:
					stack.append((cur.right, False))
					stack.append((cur, True))
					stack.append((cur.left, False))
		return result

'''
another solution by cleancode
'''
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



