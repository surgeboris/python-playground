import time


def measure(fn, times=1):
    start = time.time()
    result = [fn() for _ in range(times)][0]
    end = time.time()
    return end - start, result

if __name__ == "__main__":
    seconds, result = measure((lambda: 2 + 2), times=1000000)
    print(f"\n\n\nResult is {result}. Average time is {seconds} seconds\n\n\n")
