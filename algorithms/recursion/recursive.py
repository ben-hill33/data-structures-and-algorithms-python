# Write a function that takes an integer as an input and returns the sum of all numbers from the input down to 1

def sum_to_one(n):
    if n == 1:
        print(f"BASE CASE REACHED: {n}")
        return n

    if n != 1:
        print(f"Recursing with input: {n}")
        return n + sum_to_one(n - 1)

print(sum_to_one(4))
