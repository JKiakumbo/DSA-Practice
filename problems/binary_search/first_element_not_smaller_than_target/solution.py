from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
