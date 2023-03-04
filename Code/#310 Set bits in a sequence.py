"""
Write an algorithm that finds the total number of set bits in all integers between 1 and N, inclusive.
"""
from chrono import chrono

def bits_set_in(number: int) -> list:
    
    if (number < 0):
        return None
    
    bits_set: list[int] = []
    
    aux_number: int = number
    bit_index: int = 0
    while (aux_number > 0):
        is_set: bool = aux_number & 1
        if (is_set):
            bits_set.append(bit_index)
        aux_number >>= 1
        bit_index += 1
    return bits_set

def number_of_bits_set_in(number: int) -> int:
    if (number < 0):
        return -1
    
    aux_number: int = number
    bits_set = 0
    while (aux_number > 0):
        bits_set += aux_number & 1
        aux_number >>= 1
    return bits_set

def naive_history_of_bits_set_until(number: int):
    if (number < 0):
        return -1
    
    accumulator = 0
    for i in range(1, number+1):
        accumulator += number_of_bits_set_in(i)
    return accumulator

def history_of_bits_set_for_powers_of_two():
    history = 1
    yield history

    offset = 0
    while True:
        history *= 2
        history += offset

        offset *= 2
        offset += 1
        
        yield history

def history_approach_and_count(number: int):
    if (number < 0):
        return -1
    
    if (number == 0):
        return 0
    
    exponent_of_two = 0
    power_of_two = 1

    while (power_of_two <= number):
        power_of_two *= 2
        exponent_of_two += 1
    
    # Too far; recoil just one step
    exponent_of_two -= 1
    power_of_two //= 2
    
    bits_set_history = history_of_bits_set_for_powers_of_two()
    for _ in range(exponent_of_two):
        next(bits_set_history)
    
    accumulator = next(bits_set_history)
    for i in range(power_of_two+1, number+1):
        accumulator += number_of_bits_set_in(i)
    
    return accumulator

def history_approach_and_count_from_number_bits(number: int):
    if (number < 0):
        return -1
    
    if (number == 0):
        return 0
    
    bits_in_number = bits_set_in(number)
    last_bit = bits_in_number[-1]

    bits_set_history = history_of_bits_set_for_powers_of_two()
    for _ in range(last_bit):
        next(bits_set_history)

    accumulator = next(bits_set_history)
    if (len(bits_in_number) != 1):
        accumulator += len(bits_in_number)

    power_of_two = 2**last_bit
    for i in range(power_of_two+1, number):
        accumulator += number_of_bits_set_in(i)

    return accumulator

def lock_histories(number: int):
    if (number < 0):
        return -1
    
    if (number == 0):
        return 0
    
    bits_set_in_number = bits_set_in(number)
    bits_set_in_number.reverse()

    history = history_of_bits_set_for_powers_of_two()
    histories = [ next(history) for _ in range(bits_set_in_number[0]+1) ]

    accumulator = 0
    for locked_bits, bit in enumerate(bits_set_in_number):
        accumulator += histories[bit]
        accumulator += locked_bits * (2**bit)

    return accumulator

if __name__ == "__main__":
    # history = history_of_bits_set_for_powers_of_two()
    # for i in range(20):
    #     #print("NEW LOOP with", i)
    #     aux_i = i
    #     while (aux_i > 1 and aux_i % 2 == 0):
    #         aux_i //= 2
    #         #print("Aux_i:", aux_i)

    #     if (aux_i == 1):
    #         print(i, "=>", lock_histories(i), naive_history_of_bits_set_until(i), ";", next(history))
    #     else: 
    #         print(i, "->", lock_histories(i), naive_history_of_bits_set_until(i))
    
    number = 10000000
    print(chrono(lock_histories, [number], "Lock histories"))
    print(chrono(history_approach_and_count_from_number_bits, [number], "History approach with index from other function"))
    print(chrono(history_approach_and_count, [number], "History approach"))
        
