from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(arr):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1
    return slow + 1
