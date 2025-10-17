def subarray_sum_longest(nums: list[int], target: int) -> int:
    ans = 0
    left = 0
    window_sum = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > target:
            window_sum -= nums[left]
            left += 1

        if window_sum <= target:
            ans = max(ans, right - left + 1)

    return ans