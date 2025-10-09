# Container With Most Water

## Problem Metadata
- **Name:** Container With Most Water
- **Link:** https://algo.monster/problems/container_with_most_water
- **Difficulty:** Medium
- **Pattern:** Two Pointers
- **Tags:** two-pointers, array, container-with-most-water

## Key Dates
- **First Attempt:** 09-10-2025
- **Solved On:** 09-10-2025
- **Time Spent:** 20 minutes

## Solution
```python
def container_with_most_water(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(arr[left], arr[right])
        max_area = max(max_area, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

## Approach Steps
1. Initialize two pointers, `left` at the start and `right` at the end of the array.
2. Initialize a variable `max_area` to keep track of the maximum area found.
3. While `left` is less than `right`, calculate the area formed by the lines at these pointers.
4. Update `max_area` if the calculated area is greater than the current `max_area`.
5. Move the pointer pointing to the shorter line inward (increment `left` if `arr[left] < arr[right]`, else decrement `right`).
6. Repeat steps 3-5 until the pointers meet.
7. Return `max_area` after the loop.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The two-pointer technique is effective for problems involving pairs of elements in an array.
- Moving pointers based on the comparison of the heights helps efficiently find the maximum area.
- The problem can be solved in linear time without additional space.
- Ensure to handle edge cases where the array has less than two elements.

### What Worked Well
- Clear understanding of the container with most water problem.
- Efficiently used two pointers to find the solution.
- Handled edge cases correctly.

### Challenges Faced
- None significant.

### For Next Time
- Remember to always check for edge cases, such as when the array has less than two elements.
- Practice more two-pointer variations.
- Review problems involving area calculations and optimization.
