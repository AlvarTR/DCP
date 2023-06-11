"""
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.
"""
from collections import deque
from timeit import timeit
from typing import List
from itertools import product

import numpy as np


def parse_states_to_list_of_wheels(initial_state: str,
                                   desired_state: str,
                                   deadlock_states: List[str]):
    wheels = np.array([int(char) for char in initial_state],
                      dtype=np.int8)

    desired_wheels = np.array([int(char) for char in desired_state],
                              dtype=np.int8)

    deadlocks = [np.array([int(char) for char in deadlock], dtype=np.int8)
                 for deadlock in deadlock_states]

    return wheels, desired_wheels, deadlocks


def turn_direction_and_steps_dict(wheels, desired_wheels):
    wheels_raw_options = np.array([desired_wheels - wheels,
                                   wheels - desired_wheels])

    wheels_options = np.where(wheels_raw_options < 0,
                              -(wheels_raw_options + 10),
                              wheels_raw_options)

    options_dict = {}
    for chooser in product(range(wheels_options.shape[0]), repeat=wheels_options.shape[1]):
        options = np.choose(chooser, wheels_options)
        options_dict[tuple(np.sign(options))] = options

    return options_dict


def all_first_move_options(turn_and_steps_dict: dict) -> deque:
    state_list = []
    for current_option in (np.stack([value, np.array(key)])
                           for key, value in turn_and_steps_dict.items()):
        for i, direction in enumerate(current_option[-1]):
            new_option = current_option.copy()
            new_option[0, i] -= direction
            state_list.append(new_option)

    return state_list


def direct_unlock(initial_state: str,
                  desired_state: str,
                  deadlock_states: List[str]):
    wheels, desired_wheels, deadlocks = parse_states_to_list_of_wheels(initial_state,
                                                                       desired_state,
                                                                       deadlock_states)
    working_wheels = np.array(wheels, copy=True)

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

            # print(working_wheels)

            for deadlock in deadlocks:
                if ((working_wheels == deadlock).all()):
                    # print("DEADLOCK")
                    return None
            total_moves += 1

        # total_moves += min(abs(option[1:]) for option in options)
    # print(total_moves)
    return total_moves


def width_unlock(initial_state: str,
                 desired_state: str,
                 deadlock_states: List[str]):
    wheels, desired_wheels, deadlocks = parse_states_to_list_of_wheels(initial_state,
                                                                       desired_state,
                                                                       deadlock_states)
    turn_and_steps_dict = turn_direction_and_steps_dict(wheels, desired_wheels)

    # The desired state and the wheel state are the same
    if (0, 0, 0) in turn_and_steps_dict:
        return 0

    state_list = all_first_move_options(turn_and_steps_dict)
    state_queue = deque()
    for current_option in state_list:
        current_wheels = (wheels + current_option[0]) % 10

        if (current_wheels == wheels).all():
            return 1

        if any((current_wheels == deadlock).all() for deadlock in deadlocks):
            # print(candidate, "initial DEADLOCK")
            continue

        state_queue.append(current_option)
    del state_list

    # All queue states are valid. No more deadlock states in the queue.

    checked = set()
    solutions = []
    while (state_queue):
        current_option = state_queue.popleft()
        for i, direction in enumerate(current_option[-1]):
            candidate = current_option.copy()
            candidate[0, i] -= direction

            hashable_candidate = tuple(tuple(row) for row in candidate)

            if hashable_candidate in checked:
                # print(candidate, "already checked. Dropping it.")
                continue

            checked.add(hashable_candidate)

            if ((candidate[0] >= 10) | (candidate[0] <= -10)).any():
                # print(candidate, "two loops of the same wheel. Dropping it")
                continue

            current_wheels = (wheels + candidate[0]) % 10

            if any((current_wheels == deadlock).all() for deadlock in deadlocks):
                # print(candidate, "DEADLOCK")
                continue

            if (current_wheels == wheels).all():
                moves_required = turn_and_steps_dict[tuple(candidate[-1])]
                # total_moves = np.sum(np.abs(moves_required))
                solutions.append(moves_required)
                continue

            state_queue.append(candidate)

    if solutions:
        print("Solutions found:")
        for solution in solutions:
            print(solution)
    else:
        print("No route found for achieving the unlock code")

    return solutions


def depth_unlock(initial_state: str,
                 desired_state: str,
                 deadlock_states: List[str]):
    wheels, desired_wheels, deadlocks = parse_states_to_list_of_wheels(initial_state,
                                                                       desired_state,
                                                                       deadlock_states)
    turn_and_steps_dict = turn_direction_and_steps_dict(wheels, desired_wheels)

    # The desired state and the wheel state are the same
    if (0, 0, 0) in turn_and_steps_dict:
        return 0

    messy_state_list = all_first_move_options(turn_and_steps_dict)

    state_list = []
    for state in sorted(messy_state_list, key=lambda x: np.sum(np.abs(x)), reverse=True):
        current_wheels = (wheels + state[0]) % 10

        if (current_wheels == wheels).all():
            return 1

        if any((current_wheels == deadlock).all() for deadlock in deadlocks):
            continue

        state_list.append(state)
    del messy_state_list

    checked = set()
    solutions = []
    # All queue states are valid. No more deadlock states in the queue.
    while state_list:
        state = state_list.pop()
        for i, direction in enumerate(state[-1]):
            candidate = state.copy()
            candidate[0, i] -= direction

            hashable_candidate = tuple(tuple(row) for row in candidate)

            if hashable_candidate in checked:
                # print(candidate, "already checked. Dropping it.")
                continue

            checked.add(hashable_candidate)

            if ((candidate[0] >= 10) | (candidate[0] <= -10)).any():
                # print(candidate, "a whole locker loop. Dropping it")
                continue

            current_wheels = (wheels + candidate[0]) % 10

            if any((current_wheels == deadlock).all() for deadlock in deadlocks):
                # print(candidate, "DEADLOCK")
                continue

            if (current_wheels == wheels).all():
                moves_required = turn_and_steps_dict[tuple(candidate[-1])]
                # total_moves = np.sum(np.abs(moves_required))
                solutions.append(moves_required)
                continue

            state_list.append(candidate)

    if solutions:
        print("Solutions found:")
        for solution in solutions:
            print(solution)
    else:
        print("No route found for achieving the unlock code")

    return solutions


if __name__ == "__main__":
    # timeit('direct_unlock("000", "876", ["877",])',
    #        globals=globals(), number=1)
    initial_state = "000"
    desired_state = "999"

    deadlocks = set()
    deadlocks.update("".join(p) for p in product("901", repeat=3))
    deadlocks.discard(initial_state)
    deadlocks.discard(desired_state)
    deadlocks.discard("001")

    # for a in "9":
    #     for b in "901":
    #         for c in "901":
    #             deadlocks.discard(a+b+c)
    
    print(timeit(f'depth_unlock("{initial_state}", "{desired_state}", {deadlocks})',
                 globals=globals(), number=1))
    print(timeit(f'width_unlock("{initial_state}", "{desired_state}", {deadlocks})',
                 globals=globals(), number=1))
    pass
