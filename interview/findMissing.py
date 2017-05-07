def missing(array):
    result = [0] * len(array)
    for i in array:
        result[i] += 1
    return [j for j in range(len(array)) if result[j] == 0]

print missing([0, 1, 0, 4, 1])
## time: O(n)
## space: O(n)

