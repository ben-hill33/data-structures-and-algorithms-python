class ShellSort:
    """
    An extension of insertion sort.\n
    Divides collection into smaller collections and sorts\n
    them using an insertion sort algorithm.\n
    As the algorithm progresses, the sub-collections become\n
    increasingly sorted, leading to a more efficient final\n
    insertion sort pass.\n
    Time Complexity:
        Depends on the gap sequence used (can range from O(n log^2 n) to O(n^2))\n
    Space Complexity:
        O(1)
    """

    @staticmethod
    def sort(list):
        num_records = len(list)

        # keep cutting the gap size in half as an integer -- using //
        gap = num_records // 2;
        while gap > 0:
            for i in range(gap, num_records):
                temp = list[i]
                j = i;

                while j >= gap and temp < list[j - gap]:
                    list[j] = list[j - gap]
                    j -= gap;

                list[j] = temp

            # cut gap in half as an integer -- using //
            gap = gap // 2
