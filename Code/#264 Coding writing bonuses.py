"""
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""
def bonusForLinesWritten(array):
    if not array:
        return []

    lenArray = len(array)
    bonuses = [0]*lenArray
    
    return bonuses

if __name__ == "__main__":
    arraysAndResults = (
    ([10, 40, 200, 1000, 60, 30], [1, 2, 3, 4, 2, 1]),
    ([2, 1, 2], [2, 1, 2]),
    ([1, 3, 2], [1, 2, 1]),
    )

    for array, result in arraysAndResults:
        assert bonusForLinesWritten(array) == result
