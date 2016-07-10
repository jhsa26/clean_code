'''
time: O(n)
space: O(n)
usually starts with o node with value 0 and take care of the basic manipulate of linkedlist
take refrence of the jiuzhang algorithm here

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
'''
class Solution:
	def addTwoNumbers(self, l1, l2):
		head = ListNode(0)
		ptr = head
		carry = 0
		while True:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			ptr.val = carry % 10
			carry = carry / 10
			if l1 or l2 or carry != 0:
				ptr.next = ListNode(carry)
				ptr = ptr.next
			else:
				break
		return head

if __name__ == '__main__':
	a, a.next, a.next.next = ListNode(3), ListNode(9), ListNode(2)
	b, b.next, b.next.next = ListNode(2), ListNode(5), ListNode(6)
	result = Solution().addTwoNumbers(a, b)
	print '{0} -> {1} -> {2}'.format(result.val, result.next.val, result.next.next.val)



