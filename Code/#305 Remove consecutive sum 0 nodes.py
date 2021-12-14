"""
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""
from chrono import chrono

def nonZeroConsecutives(lista):
    totals = []
    for num in lista:
        totals.append(0)
        for i in range(len(totals)):
            totals[i] += num
            if totals[i] == 0:
                break
        else:
            continue
        totals = totals[:i]

    numbers = totals
    for i, n in enumerate(numbers[1:]):
        numbers[i] -= n
    
    return numbers



if __name__ == "__main__":
    lists = [
    [1, 2, 3],
    [1, 2, 3, -6],
    [1, 3, 2, -2, -2, -1, 1],
    [3, 4, -7, 5, -6, 6],
    ]
    for l in lists:
        print(l, nonZeroConsecutives(l))
