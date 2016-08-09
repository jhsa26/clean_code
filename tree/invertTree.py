'''
Here it's specifically for tree (special case of graph)
recursion is like a general method (iteration is also)
backtracking is an algorithm by using recursion to solve a common problem
BFS/DFS are two ways to solve non-weighted graph related problems
binary and linked-list are both special cases for graph
they can be both solved by iteraion(stack for DFS and queen for BFS)
or using recursion by backtracking
DFS is guaranteed to find a path if exists and easy to retrieve the path 
we found, however the path may not be optimal, like not the best/shortest
BFS will always find the optimal path however hard to retrieve the path we found
DFS use less memory than BFS and the time complexity are almost the same
DFS:(for tree mostly)
Time: O(n)
Space: O(h)(h is the height of the tree)
BFS:
Time: O(n)
Space: O(n) (here mostly for tree and the nodes of the last level is around n/2 so it's O(n))
recursion DFS way
'''
class Solution(object):
	def invertTree(self, root):
		if root:
			root.left = self.invertTree(root.right)
			root.right = self.invertTree(root.left)
	return root

'''
to use python list like stack:
stack = [1, 2, 3]
stack.append() and stack.pop() both are O(1)
to use python list like queue:
1) we can use append() and pop(0) however the pop(0) will cost O(n) time
2) we can use the collection deque:
from collections import deque
queue = [1, 2, 3]
queue.append(4)
queue.popleft()
this way both methods are O(1)
stack Solution
Time: O(n)
space: O(h)
'''
class Solution(object):
	def invertTree(self, root):
		if root:
			nodes = []
			nodes.append(root)
			while nodes:
				node = nodes.pop()
				node.left, node.right = node.right, node.left
				if node.left:
					nodes.append(node.left)
				if node.right:
					nodes.append(node.right)
		return root









