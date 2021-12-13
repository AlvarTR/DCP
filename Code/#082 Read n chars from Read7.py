"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content �Hello world�, three read7() returns �Hello w�, �orld� and then ��.
"""

def read7():
    pass

def readN(n):
    readFunction = read7
    readX = 7

    minRead = n // readX
    additionalCharsToTake = n % readX

    string = ""
    for timesRead in range(minRead):
        string += readFunction()

    if additionalCharsToTake > 0:
        additionalRead = readFunction()
        string += additionalRead[:additionalCharsToTake]
    return string
