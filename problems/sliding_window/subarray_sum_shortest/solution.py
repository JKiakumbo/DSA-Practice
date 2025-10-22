def subarray_sum_shortest(nums: list[int], target: int) -> int:
    window_sum = 0
    ans = len(nums) + 1
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            ans = min(ans, right - left + 1)
            window_sum -= nums[left]
            left += 1

    if ans > len(nums): # This means we didn't find any valid subarray. This is possible if the target is larger than sum of all elements.
        return 0

    return ans