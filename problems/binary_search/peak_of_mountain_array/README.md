# The Peak of a Mountain Array

## Problem Metadata
- **Name:** Find the First True in a Sorted Boolean Array
- **Link:** https://algo.monster/problems/peak_of_mountain_array
- **Difficulty:** Medium
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search, mountain-array

## Key Dates
- **First Attempt:** 30-09-2025
- **Solved On:** 30-09-2025
- **Time Spent:** 20 minutes

## Solution
```python
from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
```

## Approach Steps
1. Initialize left and right pointers, and a variable to store boundary index
2. While left <= right, calculate mid
3. If arr[mid] > arr[mid + 1], update boundary index and move right pointer 
4. If arr[mid] <= arr[mid + 1], move left pointer
5. Return boundary index after loop

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find the peak in a mountain array
- Adjusting pointers based on mid value helps narrow down search space
- Need to handle case where peak is at the start or end of the array
- Need to ensure mid + 1 does not go out of bounds

### What Worked Well
- Clearly defined binary search logic
- Kept track of boundary index effectively
- Handled edge cases correctly
- Used mid + 1 safely within bounds

### Challenges Faced
- None significant

### For Next Time
- Practice more binary search variations
- Study edge cases in numerical problems
