"""
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""
from chrono import chrono

def nonZeroConsecutives(lista):
    totals = []
    for num in lista:
        totals.append(0)
        for i, t in enumerate(totals):
            currentValue = num + t
            if currentValue == 0:
                break
            totals[i] = currentValue
        else:
            print("i =", i)
            while len(totals) > i:
                totals.pop()
    return totals



if __name__ == "__main__":
    lists = [
    [1, 2, 3],
    [1, 2, 3, -6],
    [3, 4, -7, 5, -6, 6],
    ]
    for l in lists:
        print(l, nonZeroConsecutives(l))
