'''
here change the parameter name 'sum' to 'total' in order to 
avoid the conflict of using the "sum" function inside the program.
!!!!!!This is a wrong way to implement the problem, since the 'temp' in the 
self.pathSumHelper(root.left) already modify the temp before applied it to 
self.pathSumHelper(root.right)
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution(object):
	def pathSum(self, root, total):
		totalList = []
		self.pathSumHelper(root, total, [], totalList)
		return totalList

	def pathSumHelper(self, root, total, temp, totalList):
		if root:
			temp.append(root.val)
			if not root.left and not root.right and sum(temp) == total:
				totalList.append(temp)
			else:
				import pdb
				pdb.set_trace()
				self.pathSumHelper(root.left, total, temp, totalList)  ###
				self.pathSumHelper(root.right, total, temp, totalList)
				temp.pop()

if __name__ == '__main__':
	root = TreeNode(5)
	root.left = TreeNode(4)
	root.right = TreeNode(8)
	root.left.left = TreeNode(11)
	root.left.left.left = TreeNode(7)
	root.left.left.right = TreeNode(2)
	root.right = TreeNode(8)
	root.right.left = TreeNode(13)
	root.right.right = TreeNode(4)
	root.right.right.left = TreeNode(5)
	root.right.right.right = TreeNode(1)
	print Solution().pathSum(root, 22)
'''
forked github way to solve it:
The problem does not say the numbers are all positive
so no need for extra branching
Time: O(n)
Space: O(h)
backtracking is a general algorithm, dfs and bfs are both
leveraging the algorithm to apply to tree(graph) like structure
'''
class Solution(object):
	def pathSum(self, root, sum):
		return self.Helper(root, sum, [], [])

	def Helper(self, root, sum, valuelist, cur):
		if not root:
			return valuelist		## here return as valuelist, not None
		if not root.left and not root.right and root.val == sum:   ## pay attention to the condition root.val == sum
			valuelist.append(cur + [root.val])
			return valuelist
		cur.append(root.val)
		self.Helper(root.left, sum - root.val, valuelist, cur)
		self.Helper(root.right, sum - root.val, valuelist, cur)
		cur.pop()		## pop the element out in order to not make the left conflict the right
		return valuelist










