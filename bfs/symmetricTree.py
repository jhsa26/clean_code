## recursively
class Solution(object):
	def isSymmetric(self, root):
		if not root:
			return True
		else:
			return self.Helper(root.left, root.right)
	def Helper(self, cur1, cur2):
		if not cur1 and not cur2:
			return True
		if cur1 and cur2:
			return cur1.val == cur2.val and self.Helper(cur1.left, cur2.right) and self.Helper(cur1.right, cur2.left)
		return False

## the stop condition for bfs/dfs is respectively it's empty in stack or queue
## iterative way
## Time : O(n)
## Space: O(h) h is the height of the tree (which means worst case can be O(n) when the tree is way to skewed)
class Solution(object):
	def isSymmetric(self, root):
		if not root:
			return True
		stack = []
		stack.append(root.left, root.right)
		while stack:
			p, q = stack.pop(), stack.pop()
			if not p and not q:
				continue
			if (not p and q) or (not q and p):  ## can be simplified to be 
				return False					## if p is None or q is None or p.val != q.val
			if p.val != q.val:					##
				return False					##
			stack.append(p.right)
			stack.append(q.left)

			stack.append(p.left)
			stack.append(q.right)
		return True
