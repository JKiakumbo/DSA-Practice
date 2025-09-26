# Square Root Estimation

## Problem Metadata
- **Name:** Find the First True in a Sorted Boolean Array
- **Link:** https://algo.monster/problems/sqrt
- **Difficulty:** Medium
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search, sqrt

## Key Dates
- **First Attempt:** 26-09-2025
- **Solved On:** 26-09-2025
- **Time Spent:** 40 minutes

## Solution
```python
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
```

## Approach Steps
1. Initialize left and right pointers with 1 and n respectively, and a variable to store boundary index
2. While left <= right, calculate mid
3. If mid * mid == n, return mid
4. If mid * mid > n, update boundary index and move right pointer
5. If mid * mid < n, move left pointer
6. Return boundary index - 1 after loop

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find square roots by narrowing down the range
- Adjusting pointers based on mid value helps narrow down search space
- Need to handle case where n is a perfect square
- Need to handle case where n is 0

### What Worked Well
- Correctly identified the feasible conditions
- Kept track of boundary index effectively

### Challenges Faced
- Initialising left pointer to 1 instead of 0 to avoid unnecessary checks
- Remembering to return boundary_index - 1 for non-perfect squares
- Handling edge case for n = 0
- Understanding the difference between perfect squares and non-perfect squares

### For Next Time
- Practice more binary search variations
- Study edge cases in numerical problems
