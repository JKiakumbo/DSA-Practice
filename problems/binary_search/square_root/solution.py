def square_root(n: int) -> int:
    if n == 0:
        return 0
    left, right = 1, n
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index - 1
