'''
This method is wrong:
1. it's complicated than the correct one
2. two many pitfalls
3. not counting to the real leaf  (root.left is None and root.right is None)
'''
class Solution(object):
	def hasPathSum(self, root, total):
		return self.hasPathSumHelper(root, total, [])

	def hasPathSumHelper(self, root, total, numList):
		if root:				### pay attention to this step, case like([], 0) still does not work
			numList.append(root.val)
			if sum(numList) == total:
				return True
			if sum(numList) < total:
				return self.hasPathSumHelper(root.left, total, numList) or self.hasPathSumHelper(root.right, total, numList)
		return False

if __name__ == '__main__':
	print Solution().hasPathSum([1], 1)

'''
correct dfs way to do it
dfs algo:
function dfs(v1, v2):
	dfs(v1, v2, {})

function dfs(v1, v2, path):
	path += v1
	mark v1 as visited
	if v1 is v2:
		a path is found
	for each unvisited neighbor n of v1:
		if dfs(n, v2, path) finds a path 
	path -= v1
Time: O(n)
Space: O(h) h is the height of the tree
it's said for iteration case, dfs and bfs both have space O(V), but for recursive dfs, space is O(h) --
to be confirmed
'''
class Solution(object):
	def hasPathSum(self, root, sum):
		if not root:
			return False
		if not root.left and not root.right and root.val == sum:
			return True
		if root.val > sum:				## check if the condition will make the algorithm run faster
			return False
		return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

