# Move Zeros

## Problem Metadata
- **Name:** Move Zeros
- **Link:** https://algo.monster/problems/move_zeros
- **Difficulty:** Easy
- **Pattern:** Two Pointers
- **Tags:** two-pointers, array, move-zeros

## Key Dates
- **First Attempt:** 08-10-2025
- **Solved On:** 08-10-2025
- **Time Spent:** 40 minutes

## Solution
```python
from typing import List

def move_zeros(nums: List[int]) -> None:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow +=1
        fast += 1
```

## Approach Steps
1. Initialize two pointers, `slow` and `fast`, both starting at index 0.
2. Iterate through the array with the `fast` pointer.
3. If the element at the `fast` pointer is not zero, swap the elements at the `slow` and `fast` pointers, then increment the `slow` pointer.
4. Always increment the `fast` pointer.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Using two pointers allows for in-place modification of the array.
- The `slow` pointer tracks the position to place the next non-zero element.
- The `fast` pointer scans through the array to find non-zero elements.
- Handling edge cases such as empty arrays or arrays with all zeros.

### What Worked Well
- Good thought process for moving pointers.
- Efficient in-place updates.
- Clear logic for swapping elements.

### Challenges Faced
- Initially struggled with the condition to move the `slow` pointer.

### For Next Time
- Practice more problems involving two-pointer techniques to solidify understanding.
- Focus on edge cases in array manipulation problems.
