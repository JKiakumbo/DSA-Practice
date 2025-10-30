def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    if left == 0:
        return prefix_sum[right]

    return prefix_sum[right] - prefix_sum[left - 1]

# Using itertools.accumulate
from itertools import accumulate

def init_sum_array(nums: list[int]) -> list[int]:
    return list(accumulate(nums, initial=0))

def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    cumulative_sum = init_sum_array(nums)
    return cumulative_sum[right + 1] - cumulative_sum[left]
