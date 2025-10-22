# Flexible Size Sliding Window

## Problem Metadata
- **Name:** Flexible Size Sliding Window
- **Link:** https://algo.monster/problems/subarray_sum_shortest
- **Difficulty:** Medium
- **Pattern:** Sliding Window
- **Tags:** sliding-window, array, flexible-size, subarray-sum, shortest-subarray

## Key Dates
- **First Attempt:** 22-10-2025
- **Solved On:** 22-10-2025
- **Time Spent:** 40 minutes

## Solution
```python
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
```

## Approach Steps
1. Initialize `window_sum` to keep track of the sum of the current window, `ans` to store the length of the shortest subarray found (initialized to a value larger than the array length), and `left` pointer to the start of the window.
2. Iterate the `right` pointer from the start to the end of the array:
   - Add the element at the `right` pointer to `window_sum`.
   - While `window_sum` is greater than or equal to the `target`, update `ans` with the minimum of `ans` and the current window size (`right - left + 1`), then shrink the window from the left by subtracting the element at the `left` pointer from `window_sum` and incrementing `left`.
3. After the loop, check if `ans` is still larger than the length of the array, which indicates that no valid subarray was found. If so, return `0`.
4. Return `ans` as the length of the shortest subarray with a sum at least equal to `target`.    


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The sliding window technique is effective for problems involving contiguous subarrays with flexible sizes.
- Maintaining a running sum of the window allows for efficient updates as the window slides.
- The problem can be solved in linear time without additional space.

### What Worked Well
- Clear understanding of the sliding window concept.
- Efficiently maintained the window sum with constant time updates.


### Challenges Faced
- Initially I did compare the window sum to zero instead of target, which led to incorrect results.

### For Next Time
- Practice more problems involving sliding window techniques to solidify understanding.
- Focus on edge cases in array manipulation problems.
