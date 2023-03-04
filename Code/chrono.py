
from timeit import timeit # Maybe another option?

from time import perf_counter

def chrono(f, args, message = ""):
    chrono = perf_counter()
    value = f(*args)
    mesuredTime = perf_counter() - chrono
    print(f"{message}: {mesuredTime}")
    return value
