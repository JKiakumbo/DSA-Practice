# Remove Duplicates

## Problem Metadata
- **Name:** Remove Duplicates
- **Link:** https://algo.monster/problems/remove_duplicates
- **Difficulty:** Easy
- **Pattern:** Two Pointers
- **Tags:** two-pointers, array, duplicate-removal

## Key Dates
- **First Attempt:** 07-10-2025
- **Solved On:** 07-10-2025
- **Time Spent:** 50 minutes

## Solution
```python
from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(arr):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1
    return slow + 1
```

## Approach Steps
1. Initialize two pointers, `slow` and `fast`, both starting at index 0.
2. Iterate through the array with the `fast` pointer.
3. If the elements at `slow` and `fast` pointers are different, increment the `slow` pointer and update the element at `slow` with the element at `fast`.
4. Always increment the `fast` pointer.
5. After the loop, the `slow` pointer will be at the index of the last unique element, so return `slow + 1` as the count of unique elements.

## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Using two pointers allows for in-place modification of the array.
- The `slow` pointer tracks the position of the last unique element.
- The `fast` pointer scans through the array to find unique elements.
- Handling edge cases such as empty arrays or arrays with all duplicates.

### What Worked Well
- Clear logic for moving pointers.
- Efficient in-place updates.

### Challenges Faced
- Initially struggled with the while loop condition.
- Ensuring correct updates to the `slow` pointer.
- Remembering to return `slow + 1` instead of `slow`.

### For Next Time
- Practice more problems involving two-pointer techniques to solidify understanding.
- Focus on edge cases in array manipulation problems.
