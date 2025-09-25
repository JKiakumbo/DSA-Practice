# First Element Not Smaller Than Target

## Problem Metadata
- **Name:** Find Element in Sorted Array with Duplicates
- **Link:** https://algo.monster/problems/binary_search_duplicates
- **Difficulty:** Easy
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search

## Key Dates
- **First Attempt:** 25-09-2025
- **Solved On:** 25-09-2025
- **Time Spent:** 30 minutes

## Solution
```python
from typing import List

def find_first_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_occurrence_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_occurrence_index = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return first_occurrence_index
```

## Approach Steps
1. Initialize left and right pointers, and a variable to store boundary index
2. While left <= right, calculate mid
3. If arr[mid] is == target, update boundary index and move right pointer
4. If arr[mid] is > target, move right pointer
5. If arr[mid] is < target, move left pointer
6. Return boundary index after loop

> **Note:** `arr[mid] is >= target` is feasible condition, we need to update the boundary index only when `arr[mid] is == target`.

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
- I did not get it on first time that I should update the boundary index only if `arr[mid] == target`

### For Next Time
- Practice more binary search variations