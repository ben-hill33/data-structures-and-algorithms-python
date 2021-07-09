# Linear search is used to search for a target value in a list.
# It examines each of the elements in the list and compare them with the target value until matching the target.
# If a match is found, the linear search function will return the index of the matching element. Otherwise, the function will raise a ValueError, a special error to indicate that the value was not found.

# Pseudo code:
# For each element in the search_list
#   if element equal target value then
#       return its index
# if element is not found then
#   raise a ValueError

def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        print(search_list[idx])
        if search_list[idx] == target_value:
            return idx
    raise ValueError(f"{target_value} not in list!")

values = [12, 22, 24, 2]
print(linear_search(values, 2))
