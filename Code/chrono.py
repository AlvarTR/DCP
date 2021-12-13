import time

def chrono(f, args, message = ""):
    chrono = time.time()
    value = f(*args)
    mesuredTime = time.time() - chrono
    print(message, mesuredTime)
    return value
