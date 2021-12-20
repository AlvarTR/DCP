"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""
from sys import getsizeof

def longestSequenceOfOnes(number):
    numberSize = getsizeof(number)
    maxSequence, currentSequence = 0, 0
    mask, maskSize = 1, 1
    while maskSize <= numberSize:
        if number & mask:
            currentSequence += 1
        else:
            if maxSequence < currentSequence:
                maxSequence = currentSequence
            currentSequence = 0
        mask <<= 1
        maskSize += 1

    return max(maxSequence, currentSequence)

if __name__ == "__main__":
    numbers = [156, 31, 32, -3, -2, -1, 65535]
    for num in numbers:
        print(num, longestSequenceOfOnes(num))
