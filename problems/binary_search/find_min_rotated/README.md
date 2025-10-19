# Problem Solving Template

## Problem Metadata
- **Name:** Find Minimum in Rotated Sorted Array
- **Link:** https://algo.monster/problems/min_in_rotated_sorted_array
- **Difficulty:** Medium
- **Pattern:** Binary Search
- **Tags:** array, binary-search, rotated-array

## Key Dates
- **First Attempt:** 30-09-2025
- **Solved On:** 30-09-2025
- **Time Spent:** 20 minutes

## Solution
```python
from typing import List

def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
```

## Approach Steps
1. Initialize left and right pointers, and a variable to store boundary index
2. While left <= right, calculate mid
3. If arr[mid] is <= the last element of array, update boundary index and move right pointer 
4. If arr[mid] is > the last element of array, move left pointer

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find the minimum in a rotated sorted array
- Adjusting pointers based on mid value helps narrow down search space
- Need to handle case where array is not rotated (minimum is the first element)
- Need to handle case where all elements are the same


### What Worked Well
- Clearly defined binary search logic
- Kept track of boundary index effectively
- Handled edge cases correctly

### Challenges Faced
- None significant

### For Next Time
- Practice more binary search variations
- Review edge cases for rotated arrays
- Ensure understanding of array properties in binary search contexts
- Consider cases with duplicates and how they affect the search logic
- Visualize the array to better understand the rotation and minimum element location
