## given a sorted arraywith duplicates, output the occurrences of a number inside the array
def index(array, number, first):
    result = -1
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) /2
        if array[mid] == number:
            result = mid
            if first:
                high = mid - 1
            else:
                low = mid + 1
        if array[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return result

print index([1, 2, 2, 3, 4, 4], 2 ,True)

def occurenceNumber(array, number):
    firstindex = index(array, number, True)
    if firstindex == -1:
        return 0
    else:
        lastindex = index(array, number, False)
        return lastindex - firstindex + 1

print occurenceNumber([1, 2, 2, 2, 3, 4, 4], 2)
