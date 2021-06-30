# Write a function that removes nested lists within a list but keeps the values contained

nested_planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

# VISUAL
# flatten(nested_planets)
# ['mercury',
#  'venus',
#  'earth',
#  'mars',
#  'jupiter',
#  'saturn',
#  'uranus',
#  'neptune',
#  'pluto']

# Recursive functions need to identify a base case, and the recursive step that takes us closer to achieving the base case

# Base case:
# The element in the list does not contain a list
# Recursive step:
# The element in the list is a list itself

def flatten(my_list):
    # Intermediary variable stores elements for my_list
    result = []
    for elements in my_list:
        if isinstance(elements, list):
            print(f"List found at {elements}!")
            flatten_list = flatten(elements)
            result += flatten_list
        else:
            result.append(elements)
    return result

flatten(nested_planets)
