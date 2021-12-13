"""
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
"""

"""
The probability for both conditions to be met is the same, 1/36: 1/6 to get the first number, and 1/6 to get the second number. Being independent events, we can multiply them.

"""

import random

def feeCalculation(firstNumber, secondNumber):
    roll = random.randint(1, 7)
    fee = 1
    stoppingConditionMet = False
    while not stoppingConditionMet:
        if roll == firstNumber:
            roll = random.randint(1, 7)
            fee += 1
            if roll == secondNumber:
                stoppingConditionMet = True
        else:
            roll = random.randint(1, 7)
            fee += 1

    return fee

if __name__ == "__main__":
    iterations = 10000
    fiveFollowedBySix = []
    fiveFollowedByFive = []

    for i in range(iterations):
        fiveFollowedBySix.append( feeCalculation(5,6) )
        fiveFollowedByFive.append( feeCalculation(5,5) )

    print("Five followed by six:", sum(fiveFollowedBySix)/len(fiveFollowedBySix))
    print("Five followed by five:", sum(fiveFollowedByFive)/len(fiveFollowedByFive))
