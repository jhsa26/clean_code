## plan to use dynamic programming this time
## a classic dynamic programming problem, the question asked this time is a variation of
## the standard one, which only allows the add and delete operation
def editdistance(str1, str2):
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    array = [[0 for i in range(len1)] for j in range(len2)]
    for i in xrange(len1):
        array[0][i] = i
    for j in xrange(1, len2):
        array[j][0] = j
    for i in xrange(1, len1):
        for j in xrange(1, len2):
            array[j][i] = min(array[j][i - 1] + 1, array[j-1][i] + 1, array[j - 1][i - 1] + 2 * (str1[i - 1] != str2[j - 1]))
    return array[-1][-1]

print editdistance('VINCE', 'VENICE')
