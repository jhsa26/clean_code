''' 
Time: O(n)
space: O(1)
my verbose version 
remove the nodes together until meet the different one
'''
class Solution(object):
	def deleteDuplicates(self, head):
		if not head:
			return head
		p1 = head
		p2 = p1.next
		while p2:
			if p1.val == p2.val:
				p2 = p2.next
			else:
				p1.next = p2
				p1 = p2
				p2 = p2.next
		p1.next = None
		return head

'''
github version
which delete the duplicate node one by one
'''
class Solution(object):
	def deleteDuplicates(self, head):
		p1 = head
		while p1 and p1.next:
			if p1.next.val == p1.val:
				p1.next = p1.next.next
			else:
				p1 = p1.next
		return head
