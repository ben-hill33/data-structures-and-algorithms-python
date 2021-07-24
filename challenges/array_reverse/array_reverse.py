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

# def reverse_array(my_list):
#     reversed_list = []
#     for i in range(len(my_list)):
#         reversed_list.append(my_list[-(i + 1)])
#     return reversed_list


# def reverse_arrary_no_built_ins(my_list):
#     return [my_list[-(i + 1)] for i in range(len(my_list))]


# def reverse_array_in_place(my_list):
#     for i in range(0, len(my_list) // 2):
#         my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]
#     return my_list

my_list = [1, 2, 3, 4, 5, 6]
#      <-  ^              ^ ->
#           \             |
# start_index:[0]       end[5]


def reverse_list(my_list):
    # point to first element
    start = 0
    # point to last element
    end = len(my_list) - 1
    # length of list is 5 indexes, the minus one accounts for index, rather than value
    # length of array is 6 elements, index starts at index zero, element 6, therefore is index 5

    # swap indexes
    while end > start:
        # while its true that the end is greater than the start
        my_list[start], my_list[end] = my_list[end], my_list[start]
        # start index, being zero, will be plus one, after the switch, will be 6, 5, 4, 3, 2, 1
        start = start + 1
        # end index, being index five, while loop will break because once the end(right) reaches the middle, the end will no longer be greater than the start
        end = end - 1
