"""
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""
from chrono import chrono

# https://oeis.org/A051037
def regularNumbers(n):
    if n < 0:
        return -1
    regularNumIndex = 0
    currentRegularNum = 1
    yield currentRegularNum

    primeDivisors = (2, 3, 5)
    powers = [0, 0, 0]
    while regularNumIndex < n:
        regularNumIndex += 1

        #TODO

        currentRegularNum = 0
        for i, prime in enum(primeDivisors):
            currentRegularNum += prime**powers[i]
        yield currentRegularNum
    return #Nothing left to do
if __name__ == "__main__":
    pass
