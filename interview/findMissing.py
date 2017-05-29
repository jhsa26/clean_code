def missing(array):
    result = [0] * len(array)
    for i in array:
        result[i] += 1
    return [j for j in range(len(array)) if result[j] == 0]

print missing([0, 1, 0, 4, 1])
## time: O(n)
## space: O(n)

# if we wanna with O(n) time and in place then:
def missing(array):
    for i in range(len(array)):
        index = abs(i) - 1
        array[index] = -abs(array[index])
    return [i + 1 for i in range(len(array)) if array[i] > 0]

