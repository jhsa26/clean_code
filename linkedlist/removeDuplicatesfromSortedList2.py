'''
Time: O(n)
Space: O(1)
my version
set up a dummy node to lead the whole linked list 
use tag to identify if the certain node is duplicate
make all cases general into one while loop
'''
class Solution(object):
	def deleteDuplicates(self, head):
		tag = 0
		dummy = ListNode(0)
		dummy.next = head
		p1 = dummy
		p2 = head
		while p2 and p2.next:
			if p2.val == p2.next.val:
				tag = 1
				p2 = p2.next
			elif tag == 1:
				p1.next = p2.next
				p2 = p2.next
				tag = 0
			else:
				p1 = p2
				p2 = p2.next
		if tag == 1:
			p1.next = None
		return dummy.next

''' 
github and jiuzhang general way
two while loop, divide into two cases, the fisrt case
contain another while loop in the outer while loop
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
	def __repr__(self):
		if self is None:
			return "Null"
		else:
			return '{} -> {}'.format(self.val, repr(self.next))

class Solution(object):
	def deleteDuplicates(self, head):
		dummy = ListNode(0)
		dummy.next = head
		pre, cur = dummy, head
		while cur and cur.next:
			if cur.val == cur.next.val:
				val = cur.val
				while cur and cur.val = val:     ### be care to include cur here
					cur = cur.next
				pre.next = cur
			else:
				pre = cur
				cur = cur.next
		return dummy.next





