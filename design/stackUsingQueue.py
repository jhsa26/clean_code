'''
pay attention here that the traditional queue can only 
have append, peek, size, isEmpty() four operations!
Time: pop() and top() are O(N), others are O(1)
'''

class Stack(object):
	def __init__(self):
		self.stack = collections.deque()

	def push(self, x):
		self.stack.append(x)

	def pop(self):
		for i in range(len(self.stack) - 1):
			self.stack.append(self.stack.popleft())
		self.stack.popleft()

	def top(self):
		# return self.stack[-1] 			traditional queue does not support this
		for i in range(len(self.stack) - 1):
			self.stack.append(self.stack.popleft())
		temp = self.stack.popleft()
		self.stack.append(temp)
		return temp 

	def empty(self):
		return not self.stack
