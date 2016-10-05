class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	maxSumm = float("-inf")
	def maxSumPath(self, root):
		self.maxSum(root)
		return self.maxSumm

	def maxSum(self, root):
		if not root:
			return 0
		maxLeft = max(0, self.maxSum(root.left))
		maxRight = max(0, self.maxSum(root.right))
		self.maxSumm = max(self.maxSumm, root.val + maxLeft + maxRight)
		return root.val + max(maxLeft, maxRight)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = Solution().maxSumPath(root)
    print result