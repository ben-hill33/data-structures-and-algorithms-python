class SelectionSort:
    """
    Repeatedly selects the smallest element from the unsorted\n
    portion of the array and swaps it with the element in\n
    the current position.\n
    It repeats this process until the collection is sorted.\n
    Time Complexity:
        O(n^2)\n
    Space Complexity:
        O(1)
    """

    @staticmethod
    def sort(list):
        num_records = len(list)
        for i in range(num_records - 1):

           # Find index of smallest remaining element
           index_smallest = i
           for j in range(i + 1, num_records):

              if list[j] < list[index_smallest]:
                 index_smallest = j

           # Swap list[i] and list[index_smallest]
           temp = list[i]
           list[i] = list[index_smallest]
           list[index_smallest] = temp
