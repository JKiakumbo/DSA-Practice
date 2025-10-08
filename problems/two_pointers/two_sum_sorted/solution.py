
def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        two_sum = arr[left] + arr[right]
        if two_sum == target:
            return [left, right]
        elif two_sum < target:
            left += 1
        else:
            right -= 1

    return []
