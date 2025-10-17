def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = sum(nums[0:k])
    ans = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum += nums[right] - nums[left]
        ans = max(ans, window_sum)

    return ans