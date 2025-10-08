# Two Sum Sorted

## Problem Metadata
- **Name:** Two Sum Sorted
- **Link:** https://algo.monster/problems/two_sum_sorted
- **Difficulty:** Easy
- **Pattern:** Two Pointers
- **Tags:** two-pointers, array, sorted-array, two-sum

## Key Dates
- **First Attempt:** 08-10-2025
- **Solved On:** 08-10-2025
- **Time Spent:** 20 minutes

## Solution
```python
def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        two_sum = arr[left] + arr[right]
        if two_sum == target:
            return [left, right]
        elif two_sum < target:
            left += 1
        else:
            right -= 1

    return []
```

## Approach Steps
1. Initialize two pointers, `left` at the start and `right` at the end of the array.
2. While `left` is less than `right`, calculate the sum of the elements at these pointers.
3. If the sum equals the target, return the indices `[left, right].
4. If the sum is less than the target, increment the `left` pointer to increase the sum.
5. If the sum is greater than the target, decrement the `right` pointer to decrease the sum.
6. If no such pair is found, return an empty list.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The two-pointer technique is effective for problems involving sorted arrays.
- Moving pointers based on the comparison of the current sum with the target helps efficiently find the solution.
- The problem can be solved in linear time without additional space.
- Ensure to handle edge cases where no valid pair exists.

### What Worked Well
- Clear understanding of the two sum sorted array problem.
- Efficiently used two pointers to find the solution.
- Handled edge cases correctly.

### Challenges Faced
- None significant.

### For Next Time
- Remember to always check for edge cases, such as when the array has less than two elements.
- Practice more problems involving the two-pointer technique to strengthen understanding.
