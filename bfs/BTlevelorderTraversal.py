'''
bfs algo:
function bfs(v1, v2):
	queue := {v1}
	mark v1 as visited(for graph case)
	while queue is not empty:
		v := queue.dequeue()
		if v is v2:
			path found
		for each unvisited neighbor n of v:
			mark n as visited
			queue.enqueue(n)
bfs algo to find path will be a little different anyway
要活学活用， 不要墨守成规!!!
Time: O(n)
Space: O(n)
'''
class Solution(object):
	def levelOrder(self, root):
		if not root:
			return []
		res = []
		cur = [root]	
		while cur:
			nextLevel = []
			vals = []
			for item in cur:
				vals.append(item.val)
				if item.left:
					nextLevel.append(item.left)
				if item.right:
					nextLevel.append(item.right)
			res.append(vals)
			cur = nextLevel
		return res

