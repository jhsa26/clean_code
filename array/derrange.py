# def derrange(n):
# 	if n == 1:
# 		return 0
# 	if n == 2:
# 		return 1
# 	lis = [0, 1]
# 	for i in range(2, n):
# 		lis.append(i * (lis[i - 1] + lis[i - 2]))
# 	return lis[-1]

# for i in range(1, 10):
# 	print derrange(i)

def dsample(vec, n):
	total = sum(vec)
	avg = total/n
	res = []
	vec.sort(reverse = True)
	while vec:
		subsample = []
		index = []
		for i in range(len(vec)):
			if vec[i] + sum(subsample) > avg:
				continue
			elif vec[i] + sum(subsample) == avg:
				subsample.append(vec[i])
				index.append(i)
				res.append(subsample)
				break
			else:
				subsample.append(vec[i])
				index.append(i)
		if sum(subsample) != avg:
			raise Exception("not breakable")
		for j in sorted(index, reverse = True):
			del vec[j]
	return res



print dsample([8, 1, 2, 7, 1, 1, 1, 1, 5], 3)
print dsample([8, 1, 7, 2, 5, 5, 5, 3], 4)