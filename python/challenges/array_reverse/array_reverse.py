# Built-in method .reverse test
# Input : list = [1, 2, 3, 4, 5]
# Output : [5, 4, 3, 2, 1]

# my_list = [1, 2, 3, 4, 5]
# print("my list before reverse", my_list)

# my_list.reverse()
# print("my list after reverse", my_list)

# Using slicing technique

# my_list = [1, 2, 3, 4, 5]
# print('my list before reverse', my_list)

# my_list2 = my_list[::-1]
# print('my last after reverse', my_list)

def reverse_array(my_list):
    reversed_list = []
    for i in range(len(my_list)):
        reversed_list.append(my_list[-(i + 1)])
    return reversed_list

def reverse_arrary_no_built_ins(my_list):
    return [my_list[-(i + 1)] for i in range(len(my_list))]

def reverse_array_in_place(my_list):
    for i in range(0, len(my_list) // 2):
        my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]
    return my_list

