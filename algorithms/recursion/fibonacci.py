def fibonacci(n):
    # Base Case
    if n == 1:
        print(f"Fib at one: {n}")
        return 1
    if n == 0:
        print(f"Fib at zero: {n}")
        return 0
    # Recursively work toward base case
    return fibonacci(n - 2) + fibonacci(n - 1)

# BIG O: O(2^n) - Exponential

print(fibonacci(8))
