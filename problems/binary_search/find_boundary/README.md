# Problem Solving Template

## Problem Metadata
- **Name:** Find the First True in a Sorted Boolean Array
- **Link:** https://algo.monster/problems/binary_search_boundary
- **Difficulty:** Easy
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search

## Key Dates
- **First Attempt:** 23-09-2025
- **Solved On:** 23-09-2025
- **Time Spent:** 20 minutes

## Solution
```python
from typing import List

def first_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
```

## Approach Steps
1. Initialize left and right pointers, and a variable to store boundary index
2. While left <= right, calculate mid
3. If arr[mid] is True, update boundary index and move right pointer
4. If arr[mid] is False, move left pointer
5. Return boundary index after loop

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find boundaries in sorted arrays
- Adjusting pointers based on mid value helps narrow down search space
- Need to handle case where no True exists


### What Worked Well
- Clearly defined binary search logic
- Kept track of boundary index effectively
- Handled edge cases correctly

### Challenges Faced
- Initially confused about updating pointers
- Remembered to check for no True case
- Ensured mid calculation avoids overflow

### For Next Time
- Practice more binary search variations
- Study edge cases in sorted arrays
- Explore other boundary search problems
