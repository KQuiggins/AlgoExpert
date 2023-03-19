
import gc
import timeit


gc.enable() # Enable garbage collection`

def function_one(a):
    return 1 + a[0]



def function_two(a):
    return sum(a)


def function_three(a):
    return (a**a)

execution_time = timeit.timeit(lambda: function_one([1]), number=1)

print(f"Execution time: {execution_time:.6f} seconds")

execution_time2 = timeit.timeit(lambda: function_two([1, 2, 3]), number=1)

print(f"Execution time: {execution_time2:.6f} seconds")

execution_time3 = timeit.timeit(lambda: function_two([1, 2, 3]), number=1)

print(f"Execution time: {execution_time3:.6f} seconds")