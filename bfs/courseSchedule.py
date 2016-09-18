'''
pay attention to the three ways to represent graphs:
1. edge lists
2. adjacency matrices
3. adjacency lists
topological sort: youtube video tutorial
the problem is equivalent to check if there is a cycle in the directed graph
to give a topological ordering for a graph can be done by dfs
but this problem(find if there is a cycle) we did it by bfs
solution by: http://zhufangxing.com/2015/05/01/leetcode-ICourse%20Schedule/
Time: O(n)
Space: O(n)
'''
class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		if numCourses < 2 or len(prerequisites) < 2:
			return True
		while True:
			count = 0
			mark = [True] * numCourses
			for pre in prerequisites:
				mark[pre[0]] = False
			removeList = []
			for pre in prerequisites:
				if mark[pre[1]]:
					count += 1
					removeList.append(pre)
			for item in removeList:
				prerequisites.remove(pre)
			if not prerequisites:
				return True
			elif count == 0:
				return False

'''
when try to find the path exacyly for bfs/dfs, we need backtracking
if only a boolean result should be returned, we do not need backtracking
'''
