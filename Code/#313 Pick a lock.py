"""
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.
"""
from timeit import timeit

import numpy as np

from typing import List

def direct_unlock(initial_state: str, desired_state: str, deadlock_states: List[str]):
    wheels = [int(char) for char in initial_state]
    working_wheels = list(wheels)
    desired_wheels = [int(char) for char in desired_state]

    deadlocks = []
    for deadlock in deadlock_states:
        deadlocks.append([int(char) for char in deadlock])

    total_moves = 0
    for wheel_index, (wheel, desired_wheel) in enumerate(zip(wheels, desired_wheels)):
        options = {
            (desired_wheel - wheel) % 10: 1,
            (wheel - desired_wheel) % 10: -1
        }

        min_moves = min(options.keys())
        min_direction = options[min_moves]
        min_moves *= min_direction

        for move in range(wheel + min_direction, min_moves + min_direction, min_direction):
            working_wheels[wheel_index] = move % 10

            print(working_wheels)

            for deadlock in deadlocks:
                if (all(ww == dl for ww, dl in zip(working_wheels, deadlock))):
                    print("DEADLOCK")
                    return None
            total_moves += 1

        # total_moves += min(abs(option[1:]) for option in options)
    print(total_moves)
    return total_moves


if __name__ == "__main__":
    timeit('direct_unlock("000", "876", ["877",])', globals=globals(), number=1)
    pass
