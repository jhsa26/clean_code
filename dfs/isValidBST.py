'''
python can do this: 1 < 2 < 3 instead of 1 < 2 and 2 < 3
Time: O(n)
Space: O(1) ??? why is it log(n) ???
'''

class Solution(object):
	def isValidBST(self, root):
		return self.isValidBSThelper(root, float('-inf'), float('inf'))

	def isValidBSThelper(self, root, mini, maxi):
		if root:
			if not (root.val > mini and root.val < maxi):  ### pay attention to this condition
				return False
			return self.isValidBSThelper(root.left, mini, root.val) and 
				self.isValidBSThelper(root.right, root.val, maxi)
		return True
