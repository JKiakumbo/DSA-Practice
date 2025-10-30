# Range Sum Query - Immutable

## Problem Metadata
- **Name:** Range Sum Query - Immutable
- **Link:** https://algo.monster/problems/range_sum_query_immutable
- **Difficulty:** easy
- **Pattern:** Prefix Sum
- **Tags:** prefix-sum, array, range-sum-query

## Key Dates
- **First Attempt:** 30-10-2025
- **Solved On:** 30-10-2025

## Solution
```python
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
```

> **Considerations:** 
> - This method is particularly useful when the array is static (immutable) and there are many queries.
> - If the array is frequently updated, advanced data structures like segment trees might be more appropriate. However, they are more complex to implement and may require more memory and not often asked in interviews.

## Approach Steps
1. Create a prefix sum array where each element at index `i` contains the sum of elements from index `0` to `i` in the original array.
2. To get the sum of elements between indices `left` and `right`, use the prefix sum array:
   - If `left` is `0`, return the value at `prefix_sum[right]`.
   - Otherwise, return `prefix_sum[right] - prefix_sum[left - 1]`.
3. Alternatively, use `itertools.accumulate` to create a cumulative sum array with an initial value of `0`.
4. For the range sum query, return the difference between `cumulative_sum[right + 1]` and `cumulative_sum[left]`.


## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- The prefix sum technique allows for efficient range sum queries after an initial preprocessing step.
- Using `itertools.accumulate` simplifies the creation of the cumulative sum array.
- Understanding the indexing when using prefix sums is crucial to avoid off-by-one errors.

### What Worked Well
- Clear understanding of prefix sums and their application to range sum queries.
- Efficiently created the prefix sum array in a single pass.

### Challenges Faced
- Remembering to handle the case when `left` is `0` separately.
- Remembering to subtract 1 from left (`left - 1`) when using the prefix sum array initially, leading to incorrect results.
- Remembering to subtract the correct prefix sum for non-zero `left` indices.


### For Next Time
- Practice more problems involving prefix sums and subarray sums.
- Review edge cases for subarray sum problems.
