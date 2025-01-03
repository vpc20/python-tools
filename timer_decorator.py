import functools
import time


def performance_measure(original_function):
    # @functools.wraps(original_function)
    def wrapper(loop_val):
        """ decorates a function by measuring time for its execution"""
        start_time = time.perf_counter()
        result = original_function(loop_val)
        stop_time = time.perf_counter()
        print(f'Time elapsed: {stop_time - start_time}')
        return result
    return wrapper


@performance_measure
def long_loop(loop_value):
    for i in range(loop_value):
        pass


if __name__ == '__main__':
    long_loop(10000)
    long_loop(100000000)
