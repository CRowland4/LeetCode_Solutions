import time
from colorama import Fore


def performance_test(func1, func2, *args):
    start = time.perf_counter()
    func1(*args)
    func1_time = time.perf_counter() - start
    print(f"{func1.__name__} time: {func1_time}")

    start = time.perf_counter()
    func2(*args)
    func2_time = time.perf_counter() - start
    print(f"{func2.__name__} time: {func2_time}")

    if func1_time < func2_time:
        print(f"{Fore.GREEN}{func1.__name__} is {round((func2_time / (func2_time - func1_time)), 2)} percent faster than {func2.__name__}.")
    else:
        print(f"{Fore.GREEN}{func2.__name__} is {round((func1_time / (func1_time - func2_time)), 2)} percent faster than {func1.__name__}.")

    print('\n' + Fore.RESET)
    return
