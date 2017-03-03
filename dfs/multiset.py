def dfs(input, index, path, items):
	if path not in items:
		items.append(path)
	for i in range(index, len(input)):
		dfs(input, i + 1, path + [input[i]], items)

def multiset(input):
	items = []
	dfs(sorted(input), 0, [], items)
	return items

print multiset([1, 1, 2, 4])
