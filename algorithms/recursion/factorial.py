# Write a function factorial that, given an positive integer as input, returns the product of every integer from 1 up to the input.
# If the input is less than 2, return 1
# Evaluate big O runtime of the function:
    # big O: O(n!) Factorial, adding a loop for every element

def factorial(n):
# BASE CASE: Make a check that doesn't need to use recursion
    if n <= 1:
        print(f"BASE CASE: {n}")
        return 1
    if n >= 2:
        print(f"Recursing at {n}")
        return n * factorial(n-1)
# IF INPUT IS TOO LARGE, STACK OVERFLOW WILL OCCUR, CREATING RECURSION ERROR
# This happens because the call stack can only handle so many executions before getting bogged down for space.
print(factorial(12))

# EXECUTION CONTEXT:
# Step one: Program executes and reads line 6, seeing there's a function defined
# Step two: Program looks for function call, finds it on line 14
# Step three: Program reads line 7, since my input is 12, and n is not less than or equal to one, it continues
# Step four: Program reads line 10, and sees that 12 is greater than 2, executes changes inside condition
# Step five: Program reads line 11, printing string and input (n) to the console.
# Step six: Program reads line 12 and returns n at 12 multiplied by 11, which factorial gets by subtracting 12 by one, and reads the function again.
# Step seven: Repeat steps three through six until n = 1
# Step eight: Program reads print method and prints the value of n to the console, which should be one.
# Step nine: Program returns one to the console as the base case has been reached, and terminates
