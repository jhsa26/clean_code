class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
	def merge(self, intervals):
		out = []
		for i in sorted(intervals, key = lambda x : x.start):
			if out and i.start <= out[-1].end:
				out[-1].end = max(out[-1].end, i.end)
			else:
				out.append(i)
				for j in out:
					print j.start, j.end
		return out

print Interval(1,3).start, Interval(1, 3).end, Interval(2, 4).start, Interval(2, 4).end
print Solution().merge([Interval(1, 3), Interval(2, 4), Interval(5, 7)])