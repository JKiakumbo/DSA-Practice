def subarray_sum(arr: list[int], target: int) -> list[int]:
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []


# Follow-up Problem
from collections import Counter

def subarray_sum_total(arr: list[int], target: int) -> int:
    prefix_sums: Counter[int] = Counter()
    prefix_sums[0] = 1  # since empty array's sum is 0
    cur_sum = 0
    count = 0
    for val in arr:
        cur_sum += val
        complement = cur_sum - target
        if complement in prefix_sums:
            count += prefix_sums[complement]
        prefix_sums[cur_sum] += 1
    return count