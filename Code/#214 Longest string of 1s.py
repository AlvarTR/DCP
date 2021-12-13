"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""

#Doesn't work for negatives
def longestSequenceOfOnes(number):
    maxSequence = 0
    currentSequence = 0
    mask = 1
    numberCopy = number
    while numberCopy != 0:
        if numberCopy & mask:
            currentSequence += 1
        else:
            if maxSequence < currentSequence:
                maxSequence = currentSequence
            currentSequence = 0
        numberCopy >>= 1

    return max(maxSequence, currentSequence)

if __name__ == "__main__":
    numbers = [156, 31, 8]
    for num in numbers:
        print(num, longestSequenceOfOnes(num))
