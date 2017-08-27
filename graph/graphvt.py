def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i:[] for i in range(n)}
    print neighbors
    for v, w in edges:
        neighbors[v] += [w]
        neighbors[w] += [v]
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    print neighbors
    return not neighbors

print validTree(6, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
