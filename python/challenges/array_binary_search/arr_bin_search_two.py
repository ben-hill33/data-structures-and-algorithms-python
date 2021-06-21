def binary_search(nums, key):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        picked = nums[mid]
        if picked == key:
            return mid
        elif key < picked:
            right = mid - 1
        else:
            left = mid + 1
    return -1
