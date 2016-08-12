
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
    	if n == 0:						## pay attention to 0 case
    		return []
    	return self.dfs(1, n)
	def dfs(self, start, end):
   		if start > end:
   			return [None]				## pay attention
   		res = []
   		for i in range(start, end + 1):
   			leftTree = self.dfs(start, i - 1)		## dfs way to do this
   			rightTree = self.dfs(i + 1, end)
   			for m in leftTree:
   				for n in rightTree:
   					root = TreeNode(i)
   					root.left = m
   					root.right = n
   					res.append(root)
   		return res

