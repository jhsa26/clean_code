'''
Time: O(n)
Space: O(n)
here the time is still O(n) since the assignment will go through
all the nodes and the Space I think it's (n) not sure why
the github solution gives a log(n)
'''
class Solution(object):
	def sortedArrayToBST(self, nums):
		if not nums:
			return None
		if len(nums) == 1:             ## this part is optional but will improve the speed
			return TreeNode(nums[0])
		mid = len(nums) / 2
		parent = TreeNode(nums[mid])
		parent.left = self.sortedArrayToBST(nums[:mid])
		parent.right = self.sortedArrayToBST(nums[mid + 1:])
		return parent