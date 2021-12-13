"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

    The first row consists of the number 1.
    For each subsequent row, each element is the sum of the numbers directly above it, on either side.

For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""
from chrono import chrono
import math
import sys

def recursivePascalRow(row):
    if not isinstance(row, int):
        return []
    if row < 0:
        return [0]

    if row == 0:
        return [1]

    pascalRow = recursivePascalRow(row-1)
    pascalRow.insert(0, 0) #Hidden loop O(n) per iteration

    for i in range(len(pascalRow)-1):
        pascalRow[i] += pascalRow[i+1]
    return pascalRow

def optRecursivePascalRow(row):
    if not isinstance(row, int):
        return []
    if row < 0:
        return [0]

    if row == 0:
        return [1]

    pascalRow = recursivePascalRow(row-1)
    pascalRow.append(0)

    for i in range(row, 0, -1):
        pascalRow[i] += pascalRow[i-1]
    return pascalRow

def constSpaceRecursivePascalRow(row):
    def recPascalRow(pascalRow):
        if pascalRow[-1] != 0:
            return pascalRow

        for i in (i for i in range(len(pascalRow)-1, 0, -1) if pascalRow[i-1] != 0):
            pascalRow[i] += pascalRow[i-1]

        return recPascalRow(pascalRow)

    if row < 0:
        return [0]
    return recPascalRow([1]+[0]*row)


def iterPascalRow(row):
    if not isinstance(row, int):
        return []
    if row < 0:
        return [0]

    pascalRow = [1]
    lenPascalRow = 1
    while lenPascalRow <= row:
        pascalRow.insert(0, 0) #Hidden loop O(n) per iteration
        for i in range(lenPascalRow):
            pascalRow[i] += pascalRow[i+1]
        lenPascalRow += 1

    return pascalRow

def optIterPascalRow(row):
    if int(row) != row:
        return []
    if row < 0:
        return [0]

    pascalRow = [1]
    for i in range(1, row+1):
        pascalRow.append(0)
        for j in range(i, 0, -1):
            pascalRow[j] += pascalRow[j-1]

    return pascalRow

def constSpaceIterPascalRow(row):
    if int(row) != row:
        return []
    if row < 0:
        return [0]

    pascalRow = [1] + ([0]*row)
    for i in range(1, row+1):
        for j in range(i, 0, -1):
            pascalRow[j] += pascalRow[j-1]

    return pascalRow


def squarePascalRow(row):
    if row < 0:
        return [0]

    pascalRow = [1]*(row+1)
    for len in range(row, 1, -1):
        for l in range(1, len):
            pascalRow[l] += pascalRow[l-1]

    return pascalRow

def halfSquarePascalRow(row):
    if row < 0:
        return [0]

    halfRow = row//2
    pascalRow = [1]*(row+1)
    for len in range(row, halfRow, -1):
        for l in range(1, len):
            pascalRow[l] += pascalRow[l-1]

    for i in range(1, halfRow):
        pascalRow[i] = pascalRow[row-i]

    return pascalRow


def formulaPascalRow(row):
    def binomialCoef(n, k):
        if k == 0 or k == n:
            return 1
        if n == 0:
            return 0
        minK, maxK = sorted( (k, n-k) )

        result = math.prod( range(n, maxK, -1) )
        for div in range(minK, 1, -1):
            result //= div
        return result

    if row < 0:
        return [0]

    pascalRow = []
    for i in range(row+1):
        pascalRow.append(binomialCoef(row, i))
    return pascalRow

""" #Really expensive
def binomialCoef(n, k):
    if k == 0 or k == n:
        return 1
    if n == 0:
        return 0
    minK, maxK = sorted( (k, n-k) )

    denominators = list(range(n, maxK, -1))
    divisors = list(range(2, minK+1))
    for i, value in enumerate(denominators):
        if not divisors:
            break
        poppingList = []
        for j, div in enumerate(divisors):
            if div > value:
                break
            possibleValue = value / div
            possibleValueFloor = int(possibleValue)
            if possibleValueFloor == possibleValue:
                value = possibleValueFloor
                poppingList.append(j)
        while poppingList: #House-cleaning
            divisors.pop( poppingList.pop() )
        denominators[i] = value
    return math.prod(denominators)
    """

def optFormulaPascalRow(row):
    def binomialCoef(n, k):
        if k == 0 or k == n:
            return 1
        if n == 0:
            return 0
        minK, maxK = sorted( (k, n-k) )

        result = math.prod( range(n, maxK, -1) )
        for div in range(minK, 1, -1):
            result //= div
        return result

    if row < 0:
        return [0]
    halfRow = row//2

    pascalRow = [binomialCoef(row, i) for i in range(halfRow+1)]

    offset = (row+1) % 2 #0 if row is odd, 1 if row is even
    for i in range(halfRow - offset, -1, -1):
        pascalRow.append(pascalRow[i])

    return pascalRow


def yieldPascalRow(row):
    def binomialCoefGen(row):
        partial = 1
        yield partial

        if row == 0:
            return

        for n, k in zip(range(row, 0, -1), range(1, row+1)):
            partial *= n
            partial //= k
            yield partial

    if row < 0:
        return [0]
    return binomialCoefGen(row)

def yieldAndCopyPascalRow(row):
    def binomialCoefGen(row):
        pascalRow = [1]
        yield pascalRow[-1]

        if row == 0:
            return

        halfRow = row//2

        for n, k in zip(range(row, halfRow-1, -1), range(1, halfRow+1)):
            pascalRow.append(pascalRow[-1])
            pascalRow[-1] *= n
            pascalRow[-1] //= k
            yield pascalRow[-1]

        if row % 2 == 0:
            pascalRow.pop() #Remove odd value

        while pascalRow:
            yield pascalRow.pop()

    if row < 0:
        return [0]
    return binomialCoefGen(row)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    pascalRows = (yieldAndCopyPascalRow, yieldPascalRow, halfSquarePascalRow, constSpaceIterPascalRow, optIterPascalRow, iterPascalRow, constSpaceRecursivePascalRow, optRecursivePascalRow, recursivePascalRow, squarePascalRow, )#optFormulaPascalRow, formulaPascalRow, )
    rows = [1000]
    results = []
    for pr in pascalRows:
        for row in rows:
            #print( list(pr(row)) )

            result = chrono(lambda x: list(pr(x)), (row,), pr)
            for r in results:
                if r != result:
                    print("Problem with", pr)
                    break
                results.append(result)
