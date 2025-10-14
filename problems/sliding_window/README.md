# CFixed Size Sliding Window

## Problem Metadata
- **Name:** Fixed Size Sliding Window
- **Link:** https://algo.monster/problems/subarray_sum_fixed
- **Difficulty:** Easy
- **Pattern:** Sliding Window
- **Tags:** sliding-window, array, fixed-size, subarray-sum

## Key Dates
- **First Attempt:** 14-10-2025
- **Solved On:** 14-10-2025
- **Time Spent:** 20 minutes

## Solution
```python
def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = sum(nums[0:k])
    ans = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum += nums[right] - nums[left]
        ans = max(ans, window_sum)

    return ans
```

## Approach Steps
1. Calculate the sum of the first `k` elements to initialize the sliding window.
2. Initialize `ans` with the initial window sum.
3. Iterate `right` pointer from `k` to the end of the array:
   - Calculate the `left` pointer as `right - k`.
   - Update the `window_sum` by adding the element at the `right` pointer and subtracting the element at the `left` pointer.
   - Update `ans` with the maximum of `ans` and `window_sum`.
4. Return `ans` after the loop.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The sliding window technique is effective for problems involving contiguous subarrays.
- Maintaining a running sum of the window allows for efficient updates as the window slides.
- The problem can be solved in linear time without additional space.
- Ensure to handle edge cases where the array has less than `k` elements.

### What Worked Well
- Clear understanding of the sliding window concept.
- Efficiently maintained the window sum with constant time updates.

### Challenges Faced
- None significant.

### For Next Time
- Practice more problems involving sliding window techniques to solidify understanding.
- Focus on edge cases in array manipulation problems.
