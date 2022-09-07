from ArrayList import ArrayList

# create the array using a very small size
my_list = ArrayList(4)

# add many items and the ArrayList will automatically resize!
for item in [ 13, 42, 75, 57, 18, 16, 25, 32 ]:
    my_list.append(item)

# show the array
print("\n-- Array before operations --\n")
print("Allocation size: %d, length: %d" % (my_list.get_capacity(), my_list.get_length()))
print(my_list.get_array())

# run the loop
choice = 0
while choice != 9:
    # show menu
    print("\nMenu\n")
    print("1) Get number using index")
    print("2) Add number")
    print("3) Remove number")
    print("4) Remove number using index")
    print("5) Search for a number")
    print("6) Check to see if the ArrayList is empty")
    print("7) Show the ArrayList details")
    print("8) Clear the list")
    print("9) Exit")

    # get input
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        index = int(input("Enter index (0 to {}): ".format(my_list.get_length() - 1) ))
        print("Here is the value: {}".format(my_list.get(index)))
    elif choice == 2:
        number = int( input("Enter a number to add: ") )
        my_list.append(number)
    elif choice == 3:
        number = int( input("Enter a number to remove: ") )
        my_list.remove(number)
    elif choice == 4:
        index = int( input("Enter index for number to remove: ") )
        my_list.remove_at(index)
    elif choice == 5:
        number = int( input("Enter a number to find: ") )
        index = my_list.search(number)
        if index > -1:
            print("Number was found at index #{}".format(index))
        else:
            print("Number was not found.")
    elif choice == 6:
        if my_list.is_empty() == True:
            print("The ArrayList is empty.")
        else:
            print("The ArrayList has this many items in it: {}".format(my_list.get_length()))
    elif choice == 7:
        print("Allocation size: %d, length: %d" % (my_list.get_capacity(), my_list.get_length()))
        print(my_list.get_array())
    elif choice == 8:
        my_list.clear_list()
        print("\nThe list has been cleared (emptied).")
    elif choice == 9:
        print("\nGoodbye!")
    else:
        print("\nError. Please select from the menu.")

print()
print("-- Array after operations --")
print("Allocation size: %d, length: %d" % (my_list.get_capacity(), my_list.get_length()))
print(my_list.get_array())
