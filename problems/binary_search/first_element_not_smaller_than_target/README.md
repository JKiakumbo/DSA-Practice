# First Element Not Smaller Than Target

## Problem Metadata
- **Name:** First Element Not Smaller Than Target
- **Link:** https://algo.monster/problems/binary_search_first_element_not_smaller_than_target
- **Difficulty:** Easy
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search

## Key Dates
- **First Attempt:** 24-09-2025
- **Solved On:** 24-09-2025
- **Time Spent:** 20 minutes

## Solution
```python
from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
```

## Approach Steps
1. Initialize left and right pointers, and a variable to store boundary index
2. While left <= right, calculate mid
3. If arr[mid] is >= target, update boundary index and move right pointer
4. If arr[mid] is < target, move left pointer
5. Return boundary index after loop

> **Note:** `arr[mid] is >= target` is feasible condition

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find boundaries in sorted arrays
- Adjusting pointers based on mid value helps narrow down search space
- Need to handle case where no such element exists

### What Worked Well
- Clearly defined binary search logic
- Kept track of boundary index effectively
- Handled edge cases correctly

### Challenges Faced
- None significant

### For Next Time
- Practice more binary search variations