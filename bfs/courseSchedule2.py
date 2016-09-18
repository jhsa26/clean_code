'''
Time:O(n)
Space: O(n)
similar way compared to schedule i but with different implementation this Time
be careful not using bad behavior like the 'remove' in a list loop in the original
version of schedule i
'''
class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		degrees = [0] * numCourses
		childs = [[] for x in range(numCourses)]
		for pair in prerequisites:
			degrees[pair[0]] += 1
			childs[pair[1]].append(pair[0])
		courses = set(range(numCourses))
		flag = True
		ans = []
		while flag and len(courses):
			flag = False
			removeList = []
			for x in courses:
				if degrees[x] == 0:
					for child in childs[x]:
						degrees[child] -= 1
					removeList.append(x)
					flag = True
			for x in removeList:
				ans.append(x)
				courses.remove(x)
		return ans if len(courses) == 0 else []