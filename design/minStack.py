'''
first method, put the minimum of the first n elements on the 
second element of the input nth array into the stack, so that
every time pop or push we will always have the new minimum available
for us within constant time:
Time: O(1)
Space: O(n)
'''
class MinStack(object):

	def __init__(self):
		self.stack = []		

	def push(self, x):
		minimum = self.getMin()					## pay attention to the use of getMin() here first to avoid
		if minimum is None or x < minimum:		## extra deal with the constant time thing for getMin()
			minimum = x							## also be careful about the minimum can be None condition
		self.stack.append([x, minimum])
		
	def pop(self):
		self.stack.pop()

	def top(self):
		if not self.stack:					## take care of this condition
			return None
		return self.stack[-1][0]

	def getMin(self):
		if not self.stack:					## take care of this condition
			return None
		return self.stack[-1][1]

'''
second method, this time use another implementation.
in a sum, the first method put the minimum of first n
into the second element, however, this method, put the 
difference between the stack value and minimum as the 
real stack value and then have a global vairable minimum,
to retrieve the min or the original stack value can 
also be done in constant time.
'''
class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        
    # @return an integer
    def getMin(self):
        return self.min
