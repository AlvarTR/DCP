"""
Given an integer N, construct all possible binary search trees with N nodes.
"""
def catalanNumbersBefore(n):
    intN = int(n)
    if n != intN:
        return EH
    if intN < 0:
        return EH

    dynamicProgrammingList = [1, 1]
    for i in range(intN):
        if i >= 2:
            partialSum = 0
            for j in range(len(dynamicProgrammingList)):
                partialSum += dynamicProgrammingList[j] * dynamicProgrammingList[i -1 -j]
            dynamicProgrammingList.append(partialSum)

        yield dynamicProgrammingList[i]

def catalanNumberIndex(n):
    intN = int(n)
    if n != intN:
        return EH
    if intN < 0:
        return EH
    if intN < 2:
        return 1

    dynamicProgrammingList = [1, 1]
    for i in range(2, intN+1):
        partialSum = 0
        for j in range(len(dynamicProgrammingList)):
            partialSum += dynamicProgrammingList[j] * dynamicProgrammingList[i -1 -j]
        dynamicProgrammingList.append(partialSum)

    return dynamicProgrammingList[-1]

def possibleBSTWithNumberOfNodes(n):
    EH = None

    intN = int(n)
    if n != intN:
        return EH
    if intN < 0:
        return EH
    if intN <= 1:
        #Only one way of making a tree with less or equal than 1 node
        return 1
    #If n > 1
    return catalanNumberIndex(n)

if __name__ == "__main__":
    for n in range(100):
        print(possibleBSTWithNumberOfNodes(n))
