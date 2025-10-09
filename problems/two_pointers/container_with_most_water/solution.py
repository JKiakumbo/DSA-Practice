
def container_with_most_water(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(arr[left], arr[right])
        max_area = max(max_area, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area
