def sum_to_one(n):
    """
    Handles the call stack, which abstracts away from us

    The call stack stores each function (with its internal variables) until those functions resolve in a last in, first out order

    Execution contexts are a mapping between variable names and their values within the function during execution.

    Use a list for the call stack and a dictionary for each execution context
    """
    result = 1
    call_stack = []
    while n != 1:
        execution_context = {
            "n_value": n
        }
        call_stack.append(execution_context)
        n -= 1
        print(call_stack, f"<- Call stack's execution context at {n}")
    print("BASE CASE REACHED")
    while len(call_stack) != 0:
        return_value = call_stack.pop()
        print(return_value)
    return result, call_stack


print(f"call stack {sum_to_one(2)}")
