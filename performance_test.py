import time


def performance_test(func1, func2, arg):
    start = time.perf_counter()
    func1(arg)
    print(f"{func1.__name__} time: {time.perf_counter() - start}")

    start = time.perf_counter()
    func2(arg)
    print(f"{func2.__name__} time: {time.perf_counter() - start}")

    return
