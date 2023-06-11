"""
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.
"""
from collections import namedtuple, deque
from timeit import timeit
from typing import List

import numpy as np

Lock = namedtuple("Lock", "wheel_0_steps_remaining \
                           wheel_1_steps_remaining \
                           wheel_2_steps_remaining")


def parse_states_to_list_of_wheels(initial_state: str,
                                   desired_state: str,
                                   deadlock_states: List[str]):
    wheels = np.array([int(char) for char in initial_state],
                      dtype=np.int8)

    desired_wheels = np.array([int(char) for char in desired_state],
                              dtype=np.int8)

    deadlocks = []
    for deadlock in deadlock_states:
        deadlocks.append(np.array([int(char) for char in deadlock],
                                  dtype=np.int8))

    return wheels, desired_wheels, deadlocks


def turn_direction_and_steps_dict(wheels, desired_wheels):
    wheels_raw_options = np.array([desired_wheels - wheels,
                                   wheels - desired_wheels])

    wheels_options = np.where(wheels_raw_options < 0,
                              -(wheels_raw_options + 10),
                              wheels_raw_options)

    options_dict = {}
    for i in range(2):
        wheel_0_option = wheels_options[i, 0]
        wheel_0_sign = np.sign(wheel_0_option)
        for j in range(2):
            wheel_1_option = wheels_options[j, 1]
            wheel_1_sign = np.sign(wheel_1_option)
            for k in range(2):
                wheel_2_option = wheels_options[k, 2]
                wheel_2_sign = np.sign(wheel_2_option)

                options_dict[(wheel_0_sign,
                              wheel_1_sign,
                              wheel_2_sign)] = np.array([wheel_0_option, wheel_1_option, wheel_2_option])
    return options_dict

def all_first_move_options(turn_and_steps_dict: dict) -> deque:

    state_queue = deque(np.stack([value, np.array(key)]) for key, value in turn_and_steps_dict.items())
    
    queue_size_saved = len(state_queue)
    for _ in range(queue_size_saved):
        current_option = state_queue.popleft()
        for i, direction in enumerate(current_option[-1]):
            new_option = current_option.copy()
            new_option[0, i] -= direction
            state_queue.append(new_option)

    return state_queue 

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

            print(working_wheels)

            for deadlock in deadlocks:
                if ((working_wheels == deadlock).all()):
                    print("DEADLOCK")
                    return None
            total_moves += 1

        # total_moves += min(abs(option[1:]) for option in options)
    print(total_moves)
    return total_moves


def width_unlock(initial_state: str,
                   desired_state: str,
                   deadlock_states: List[str]):
    wheels, desired_wheels, deadlocks = parse_states_to_list_of_wheels(initial_state,
                                                                       desired_state,
                                                                       deadlock_states)
    turn_and_steps_dict = turn_direction_and_steps_dict(wheels, desired_wheels)

    total_moves = 0
    # The desired state and the wheel state are the same
    if (0, 0, 0) in turn_and_steps_dict:
        return total_moves

    total_moves += 1
    state_queue = all_first_move_options(turn_and_steps_dict)
    queue_len_saved = len(state_queue)

    found_deadlock: bool = False
    for _ in range(queue_len_saved):
        current_option = state_queue.popleft()
        current_wheels = (wheels + current_option[0]) % 10

        if (current_wheels == wheels).all():
            return total_moves

        found_deadlock = False
        for deadlock in deadlocks:
            if (current_wheels == deadlock).all():
                found_deadlock = True
                break

        if found_deadlock:
            continue
        
        state_queue.append(current_option)
    # All queue states are valid. No more deadlock states in the queue.
    while(state_queue):
        current_option = state_queue.popleft()
        for i, direction in enumerate(current_option[-1]):
            candidate = current_option.copy()
            candidate[0, i] -= direction

            current_wheels = (wheels + candidate[0]) % 10
            if (current_wheels == wheels).all():
                moves_required = turn_and_steps_dict[tuple(candidate[-1])]
                print("Required:", moves_required)
                total_moves = np.sum(np.abs(moves_required))
                print("Total:", total_moves)
                return total_moves

            found_deadlock = False
            for deadlock in deadlocks:
                if (current_wheels == deadlock).all():
                    found_deadlock = True
                    break

            if found_deadlock:
                continue
            
            state_queue.append(candidate)

    # No route found for achieving the unlock code
    return None


if __name__ == "__main__":
    # timeit('direct_unlock("000", "876", ["877",])',
    #        globals=globals(), number=1)
    print(timeit('width_unlock("000", "876", ["877",])',
           globals=globals(), number=1))
    pass
