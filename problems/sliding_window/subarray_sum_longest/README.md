# Flexible Size Sliding Window - Longest

## Problem Metadata
- **Name:** Flexible Size Sliding Window - Longest
- **Link:** https://algo.monster/problems/subarray_sum_longest
- **Difficulty:** Easy
- **Pattern:** Sliding Window
- **Tags:** sliding-window, array, flexible-size, subarray-sum

## Key Dates
- **First Attempt:** 17-10-2025
- **Solved On:** 17-10-2025
- **Time Spent:** 20 minutes

## Solution
```python
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
```

## Approach Steps
1. Initialize `ans` to store the length of the longest subarray, `left` pointer to the start of the window, and `window_sum` to keep track of the sum of the current window.
2. Iterate the `right` pointer from the start to the end of the array:
   - Add the element at the `right` pointer to `window_sum`.
   - While `window_sum` exceeds the `target`, shrink the window from the left by subtracting the element at the `left` pointer from `window_sum` and incrementing `left`.
   - If `window_sum` is less than or equal to `target`, update `ans with the maximum of `ans` and the current window size (`right - left + 1`.
3. Return `ans` after the loop.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The sliding window technique is effective for problems involving contiguous subarrays with flexible sizes.
- Maintaining a running sum of the window allows for efficient updates as the window expands and contracts.
- The problem can be solved in linear time without additional space.

### What Worked Well
- Clear understanding of the sliding window concept.
- Efficiently maintained the window sum with constant time updates.


### Challenges Faced
- Initially I did not consider to add 1 to the window size calculation which is crucial for correct length computation.

### For Next Time
- Practice more problems involving sliding window techniques to solidify understanding.
- Focus on edge cases in array manipulation problems.
