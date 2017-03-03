def spiralMatrix(matrix):
    if not matrix:
        return None
    colbegin, colend, rowbegin, rowend = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    res = []
    while colbegin <= colend and rowbegin <= rowend:
        for i in range(colbegin, colend + 1):
            res.append(matrix[rowbegin][i])
            print matrix[rowbegin][i]
        rowbegin += 1
        for i in range(rowbegin, rowend + 1):
            res.append(matrix[i][colend])
            print matrix[i][colend]
        colend -= 1
        if rowbegin <= rowend:
            for i in range(colend, colbegin - 1, -1):
                print matrix[rowend][i]
                res.append(matrix[rowend][i])
            rowend -= 1
        print colbegin, colend, rowend, rowbegin
        if colbegin <= colend:
            for i in range(rowend, rowbegin - 1, -1):
                print matrix[i][colbegin]
                res.append(matrix[i][colbegin])
            colbegin += 1
    return res

print spiralMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
