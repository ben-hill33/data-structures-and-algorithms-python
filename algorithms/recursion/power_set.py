# A power set is a list of all subsets of the values in a list
# Requires a runtime of at least O(2^n) (quadratic)
    # Producing subsets will never be better than that because because a set of N elements creates a power set of 2^n elements

# MOST BASIC POWER SET:
# Base case = empty list
# power_set([])

# Recursive step needs to progress towards base case, an empty list
# A power set in the recursive step requires:
    # all subsets which contain the element
        # power_set(['a'])
    # all subsets which don't contain the element, in this case, the empty list

def power_set(my_list):
    # base case: empty list
    if len(my_list) == 0:
        print(f"BASE CASE: {my_list}")
        return [[]]
    # recursive step: subset without first element
    power_set_without_first = power_set(my_list[1:])
    # subset with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first

random_nums = ['ONE', 'TWO', 'THREE', 'FOUR']
power_set_of_random_nums = power_set(random_nums)

for set in power_set_of_random_nums:
    print(set)
