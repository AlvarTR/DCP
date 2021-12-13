"""
Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2 = c2.
"""
from chrono import chrono
import math

def pythagoreanTripletsInArrayNaive(array):
    pythagoreanResults = []
    lenArray = len(array)
    for i, a in enumerate(array):
        aSquared = a*a
        for b in array[i+1:]:
            aPlusB = b*b + aSquared
            for c in array:
                cSquared = c*c
                if aPlusB == cSquared:
                    pythagoreanResults.append( (a, b, c) )
    return pythagoreanResults

def pythagoreanTripletsInArraySorted(array):
    pythagoreanResults = []
    sortedArray = sorted(array, reverse = True)
    for i, c in enumerate(sortedArray):
        cSquared = c*c
        halfCSquared = cSquared//2
        for j, b in enumerate(sortedArray[i+1:], i+1):
            bSquared = b*b
            if halfCSquared > bSquared:
                break
            for a in sortedArray[j+1:]:
                aPlusB = a*a + bSquared
                if cSquared > aPlusB:
                    break
                if cSquared != aPlusB:
                    continue
                pythagoreanResults.append( (a, b, c) )
    return pythagoreanResults

def pythagoreanTripletsInArrayHash(array):
    pythagoreanResults = []

    dictionary = {}
    for number in array:
        if number not in dictionary:
            dictionary[number] = 0
        dictionary[number] += 1

    for a in dictionary:
        aSquared = a*a
        for b in (b for b in dictionary if a != b or dictionary[b] > 1):
            aPlusB = aSquared + b*b
            c = int(math.sqrt(aPlusB))
            if aPlusB != c*c:
                continue
            if c not in dictionary:
                continue
            pythagoreanResults.append( (a, b, c) )
    return pythagoreanResults

if __name__ == "__main__":
    array = list(range(500))
    chrono(pythagoreanTripletsInArrayHash, (array,), "Hash:")
    chrono(pythagoreanTripletsInArraySorted, (array,), "Sorted:")
    chrono(pythagoreanTripletsInArrayNaive, (array,), "Naive:")
