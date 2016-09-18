'''
make full use of the peek function, also make another temp to collect
the reversed data structure
'''
class Queue(object):
	def __init__(self):
		self.queue = []
		self.temp = []

	def push(self, x):				### add more to queue, but pop and peek using temp, then temp is empty, reinput the elements in 
									### in queue to the temp stack reversely
		self.queue.append(x)

	def pop(self):
		self.peek()
		self.temp.pop()

	def peek(self):
		if not self.temp:
			while self.queue:
				self.temp.append(self.queue.pop())
		return self.temp[-1]

	def empty(self):
		return not self.queue
