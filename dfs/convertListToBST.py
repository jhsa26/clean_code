'''
be careful for the two front cases,
what's more the dummy variable is used for the case of two nodes left
and the temp will be null in that case
time: O(n)
space: O(n)
'''
class Solution(object):
	def sortedListToBST(self, head):
		if not head:
			return None
		if not head.next:
			return TreeNode(head.val)
		dummy = TreeNode(0)    
		dummy.next = head
		slow, fast = dummy, head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next
		temp = slow.next
		slow.next = None
		middle = TreeNode(temp.val)
		middle.left = self.sortedListToBST(head)
		middle.right = self.sortedListToBST(temp.next)
		return middle

