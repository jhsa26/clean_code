class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	head = None
	def convertListToTree(self, head):
		length = 0
		curr = head
		while curr:
			curr = curr.next
			length += 1
		self.head = head
		return self.bottomFirst(0, length)
    
    def bottomFirst(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        left = self.bottomFirst(start, mid)
        current = TreeNode(self.head.val)
        current.left = left 
        self.head = self.head.next
        current.right = self.bottomFirst(mid + 1, end)
        return current
